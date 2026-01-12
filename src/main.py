from fastapi import FastAPI
from contextlib import asynccontextmanager

from book.routes import bookRouter
from db.main import init_db

@asynccontextmanager
async def life_span(app:FastAPI):
    print(f"Server is running....")
    await init_db()
    yield
    print(f"Server has been stopped....")

version = "v1"

app = FastAPI(
    title="Bookly",
    description="A Book REST API for the Bookly",
    version=version,
    lifespan=life_span
)

app.include_router(bookRouter,prefix=f"/api/{version}/books",tags=["books"])
