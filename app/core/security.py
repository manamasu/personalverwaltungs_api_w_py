from passlib.context import CryptContext

# Quelle:
# https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html#basic-usage
# https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#hash-and-verify-the-passwords
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_value(password: str) -> str:
    return pwd_context.hash(password)


def verify_value(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)
