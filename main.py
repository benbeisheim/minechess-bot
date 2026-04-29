from fastapi import FastAPI
from contextlib import asynccontextmanager
import maia
from bot import get_move

@asynccontextmanager
async def lifespan(app: FastAPI):
    maia.initialize()
    yield

app = FastAPI(lifespan=lifespan)

@app.post("/moves")
def get_move_probs(fen: str, difficulty: int):
    return get_move(fen, difficulty)

