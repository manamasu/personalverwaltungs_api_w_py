from datetime import datetime, timedelta, timezone
import jwt

from app.config import get_settings

settings = get_settings()


# TODO: Code is pretty similar to refresh_access_token (method), need to be refactored.
def create_access_token(data: dict):
    to_encode = data.copy()
    # Quelle für JWT: https://pyjwt.readthedocs.io/en/stable/usage.html#expiration-time-claim-exp
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        payload=to_encode, key=settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt


def create_refresh_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.REFRESH_TOKEN_EXPIRE_DAYS
    )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        payload=to_encode, key=settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt


def verify_token(token: str) -> str:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
        return payload
    except jwt.ExpiredSignatureError | jwt.DecodeError:
        print("expired")
        raise ValueError("Ungültiger oder abgelaufener Token")
