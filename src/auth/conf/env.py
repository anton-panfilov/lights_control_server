from pydantic_settings import BaseSettings


class EnvConf(BaseSettings):
    JWT_SECRET: str = ""
    JWT_SECRET_OLD: str = ""
    JWT_ALGORITHM: str = "EdDSA"


env = EnvConf()
