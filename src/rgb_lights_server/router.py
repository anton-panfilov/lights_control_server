from fastapi import APIRouter, Response, Depends
from pydantic import BaseModel

from src.auth.auth.auth_bearer import JWTBearer
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
