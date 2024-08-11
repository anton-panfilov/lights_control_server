import time
from json import JSONDecodeError

from fastapi import APIRouter, Request, Response, Depends, HTTPException
from pydantic import BaseModel

from src.auth.auth.auth_bearer import JWTBearer
from src.rgb_lights_server.env import env
from src.rgb_lights_server.slack_bot import signature_verifier, EMOJI_TO_COLOR, SlackEventExample
from src.rgb_lights_server.statement import RGB, statement

router = APIRouter()


class SetColorResponse(BaseModel):
    success: bool
    next_change_available_in: float


class SynchronizeColorReceivingResponse(BaseModel):
    seconds_until_next_sync: float


@router.get("/get-color")
async def get_color() -> RGB:
    return statement.get_color()


@router.post(
    path="/set-color",
    dependencies=[Depends(JWTBearer())],
    response_model=SetColorResponse,
    responses={
        200: {
            "description": "Successful Response",
            "content": {
                "application/json": {
                    "schema": {
                        "$ref": "#/components/schemas/SetColorResponse"
                    },
                    "example": {
                        "success": True,
                        "next_change_available_in": 9.999821
                    }
                }
            }
        },
        423: {
            "description": "Resource is locked. Another change cannot be made at this time.",
            "content": {
                "application/json": {
                    "schema": {
                        "$ref": "#/components/schemas/SetColorResponse"
                    },
                    "example": {
                        "success": False,
                        "next_change_available_in": 1.232121
                    }
                }
            }
        }
    }
)
async def set_color(color: RGB, response: Response) -> SetColorResponse:
    success = statement.set_color(color)
    if not success:
        response.status_code = 423

    return SetColorResponse(
        success=success,
        next_change_available_in=statement.next_change_available_in()
    )


@router.get("/synchronize-color-receiving")
async def synchronize_color_receiving() -> SynchronizeColorReceivingResponse:
    return SynchronizeColorReceivingResponse(
        seconds_until_next_sync=statement.seconds_until_next_sync()
    )


@router.post("/slack/events")
async def slack_events(request: Request, response: Response) -> SetColorResponse:
    # # Verify Slack request signature
    # headers = {key: value for key, value in request.headers.items()}
    # if not signature_verifier.is_valid_request(await request.body(), headers):
    #     raise HTTPException(status_code=400, detail="Invalid request signature")
    #
    # # Check request timestamp to prevent replay attacks
    # timestamp = request.headers.get("X-Slack-Request-Timestamp")
    # if abs(time.time() - int(timestamp)) > 60 * 5:  # 5 minutes tolerance
    #     raise HTTPException(status_code=400, detail="Request too old")

    # parse json
    try:
        data = await request.json()
    except JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid request body")

    # Check for the message event and correct channel
    if (
            'event' in data
            #and data['event']['type'] == 'message'
            #and data['event'].get('channel') == env.SLACK_TARGET_CHANNEL_ID
    ):
        text = data['event'].get('text', '')

        # Check if the message contains one of the target emojis
        for emoji, color in EMOJI_TO_COLOR.items():
            if emoji in text:
                success = statement.set_color(color)
                if not success:
                    response.status_code = 423

                return SetColorResponse(
                    success=success,
                    next_change_available_in=statement.next_change_available_in()
                )

    raise HTTPException(status_code=201, detail="change color not detected")
