from contextlib import asynccontextmanager
from fastapi import FastAPI
from routes.tasks import router
from database import init_db

app = FastAPI(
    title="Task API",
    description="API REST para gestión de tareas con FastAPI y MongoDB",
    version="1.0.0"
)

app.include_router(router, prefix="/tasks", tags=["Tasks"])


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


@app.get("/")
def root():
    return {"message": "Bienvenido a la API de Tareas"}
