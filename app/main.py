from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.db import session


@asynccontextmanager
async def lifespan(app: FastAPI):
    session.create_db_and_table()
    print("Database connections has worked!")
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root():
    return {"Hello": "World"}
