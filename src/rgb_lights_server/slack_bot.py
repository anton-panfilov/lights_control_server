from typing import Dict, Any

from pydantic import BaseModel, Field
from slack_sdk.signature import SignatureVerifier

from src.rgb_lights_server.env import env
from src.rgb_lights_server.statement import RGB

signature_verifier: SignatureVerifier = SignatureVerifier(env.SLACK_SIGNING_SECRET)

# Mapping of emoji to RGB values
EMOJI_TO_COLOR = {
    "green_heart": RGB(R=0, G=255, B=0),
    "blue_heart": RGB(R=0, G=0, B=255),
    "red_heart": RGB(R=255, G=0, B=0),
    "yellow_heart": RGB(R=255, G=255, B=0),
    "purple_heart": RGB(R=128, G=0, B=128),
    "black_heart": RGB(R=0, G=0, B=0),
    "white_heart": RGB(R=255, G=255, B=255),
    "orange_heart": RGB(R=255, G=165, B=0),
    "brown_heart": RGB(R=165, G=42, B=42),
}


class SlackEventExample(BaseModel):
    event: Dict[str, Any] = Field(
        ...,
        example={
            "type": "message",
            "user": "U1234567890",
            "text": ":green_heart:",
            "ts": "1623442952.000200",
            "channel": "CET89KJLB",
            "event_ts": "1623442952.000200",
            "channel_type": "channel",
        }
    )
