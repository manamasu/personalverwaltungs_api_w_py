from datetime import datetime, timezone
from typing import Optional
from sqlmodel import Field, SQLModel


# Quelle und weitere Infos: https://fastapi.tiangolo.com/tutorial/sql-databases/#create-models
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    full_name: str
    email: str = Field(unique=True, index=True)
    hashed_password: str
    refresh_token_hash: Optional[str] = None
    position: str
    is_active: bool = Field(default=True)
    is_admin: bool = Field(default=False)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
