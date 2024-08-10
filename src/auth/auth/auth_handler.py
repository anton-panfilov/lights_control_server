import jwt
from pydantic import BaseModel

from src.auth.conf.env import env


class JWTFormat(BaseModel):
    # uid: int
    email: str


def decodeJWT(token: str) -> JWTFormat:
    try:
        obj = jwt.decode(token, env.JWT_SECRET, algorithms=env.JWT_ALGORITHM)
    except Exception as exc:
        if len(env.JWT_SECRET_OLD):
            obj = jwt.decode(token, env.JWT_SECRET_OLD, algorithms=env.JWT_ALGORITHM)
        else:
            raise exc
    return JWTFormat.parse_obj(obj)
