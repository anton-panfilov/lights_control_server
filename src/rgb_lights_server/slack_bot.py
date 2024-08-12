import random
from typing import Dict, Any

from pydantic import BaseModel, Field
from slack_sdk.signature import SignatureVerifier

from src.rgb_lights_server.env import env
from src.rgb_lights_server.statement import RGB

signature_verifier: SignatureVerifier = SignatureVerifier(env.SLACK_SIGNING_SECRET)

# Mapping of emoji to RGB values
EMOJI_TO_COLOR = {
    ":green_heart:": RGB(R=0, G=255, B=0),
    ":blue_heart:": RGB(R=0, G=0, B=255),
    ":heart:": RGB(R=255, G=0, B=0),
    ":hearts:": RGB(R=255, G=0, B=0),
    ":red_heart:": RGB(R=255, G=0, B=0),
    ":yellow_heart:": RGB(R=255, G=255, B=0),
    ":purple_heart:": RGB(R=128, G=0, B=128),
    ":black_heart:": RGB(R=0, G=0, B=0),
    ":white_heart:": RGB(R=255, G=255, B=255),
    ":orange_heart:": RGB(R=255, G=165, B=0),
    ":brown_heart:": RGB(R=165, G=42, B=42),
}


colors = {
    "red": RGB(R=255, G=0, B=0),
    "blue": RGB(R=0, G=0, B=255),
    "white": RGB(R=255, G=255, B=255),
    "green": RGB(R=0, G=255, B=0),
    "yellow": RGB(R=255, G=255, B=0),
    "purple": RGB(R=128, G=0, B=128),
    "black": RGB(R=0, G=0, B=0),
    "orange": RGB(R=255, G=165, B=0),
    "brown": RGB(R=165, G=42, B=42)
}

# Dictionary with lambda functions for each emoji
EMOJI_TO_COLOR = {
    ":green_heart:": lambda: colors["green"],
    ":blue_heart:": lambda: colors["blue"],
    ":heart:": lambda: colors["red"],
    ":hearts:": lambda: colors["red"],
    ":red_heart:": lambda: colors["red"],
    ":yellow_heart:": lambda: colors["yellow"],
    ":purple_heart:": lambda: colors["purple"],
    ":black_heart:": lambda: colors["black"],
    ":white_heart:": lambda: colors["white"],
    ":orange_heart:": lambda: colors["orange"],
    ":brown_heart:": lambda: colors["brown"],
    ":art:": lambda: random.choice([
        colors["red"],
        colors["blue"],
        colors["white"],
        colors["green"],
        colors["yellow"]
    ])
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
