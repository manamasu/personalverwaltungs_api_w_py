from fastapi import APIRouter, HTTPException
from sqlmodel import select

from app.core.security import hash_password, verify_password
from app.core.auth.jwt_handler import create_access_token, create_refresh_token
from app.db.session import SessionDep
from app.models.user import User
from app.schemas.user import Token, UserRead, UserCreate, UserLogin


router = APIRouter(prefix="/users", tags=["users"])


@router.post("/register", response_model=UserRead, status_code=201)
def register_user(user_data: UserCreate, session: SessionDep):
    # First check if User exists:
    existing_user = session.exec(
        select(User).where(User.email == user_data.email)
    ).first()

    if existing_user:
        print("USER EXISTS!!!")
        raise HTTPException(status_code=400, detail="Diese Email ist bereits vergeben.")

    # Now create User:
    user = User(
        full_name=user_data.full_name,
        email=user_data.email,
        hashed_password=hash_password(user_data.password),
        position=user_data.position,  # TODO: Position needs to be defined more explicitly.
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


@router.post("/login", response_model=Token, status_code=200)
def login_user(user_data: UserLogin, session: SessionDep):
    # check if user does not exist or email is incorrect
    user = session.exec(select(User).where(User.email == user_data.email)).first()
    if not user or not verify_password(user_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Ungültige Anmeldeinformationen")

    # passed the checks, login the user

    token_payload = {"subject": str(user.id), "email": user.email}

    access_token = create_access_token(token_payload)
    refresh_token = create_refresh_token(token_payload)

    print("User has been logged in")

    return Token(access_token=access_token, refresh_token=refresh_token)


@router.delete("/delete/{user_id}", status_code=204)
def delete_user(user_id: int, session: SessionDep):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(
            status_code=404, detail="User konnte nicht gefunden werden."
        )
    session.delete(user)
    session.commit()
    return {"msg": "User deleted!"}


@router.get("/{user_id}", response_model=UserRead, status_code=200)
def get_user(user_id: int, session: SessionDep):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException("User konnte nicht gefunden werden.")
    return user
