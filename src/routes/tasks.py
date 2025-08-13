from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_tasks():
    return {"message": "Aquí listaríamos las tareas"}
