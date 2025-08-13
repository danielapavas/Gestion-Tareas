from fastapi import FastAPI
from routes import tasks

app = FastAPI(
    title="Task API",
    description="API REST para gestión de tareas con FastAPI y MongoDB",
    version="1.0.0"
)

app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])

@app.get("/")
def root():
    return {"message": "Bienvenido a la API de Tareas"}
