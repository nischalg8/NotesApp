from fastapi import FastAPI
from notes.crud import api_router
from notes.database import test_connection
import asyncio
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await test_connection()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(api_router)