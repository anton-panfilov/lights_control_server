from pydantic_settings import BaseSettings


class RGBLightsConf(BaseSettings):
    SLACK_SIGNING_SECRET: str = ""
    SLACK_TARGET_CHANNEL_ID: str = "CET89KJLB"


env = RGBLightsConf()
