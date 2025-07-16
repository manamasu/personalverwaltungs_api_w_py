from fastapi import APIRouter, HTTPException
from sqlmodel import select
from app.core.security import hash_password
from app.db.session import SessionDep
from app.models.user import User
from app.schemas.user import UserRead, UserCreate, UserLogin


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
