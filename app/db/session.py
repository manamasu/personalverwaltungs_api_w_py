from sqlmodel import SQLModel, Session, create_engine
from app.config import get_settings

settings = get_settings()

engine = create_engine(settings.database_url)


def get_session():
    with Session(engine) as session:
        yield session


def create_db_and_table():
    SQLModel.metadata.create_all(engine)
