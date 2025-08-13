from fastapi import APIRouter, HTTPException
from models import TaskCreate
from database import tasks_collection
from bson import ObjectId
from datetime import datetime

router = APIRouter()

def task_helper(task) -> dict:
    return {
        "id": str(task["_id"]),
        "title": task["title"],
        "description": task.get("description"),
        "done": task["done"],
        "created_at": task["created_at"]
    }

@router.get("/")
async def list_tasks():
    tasks = []
    async for task in tasks_collection.find():
        tasks.append(task_helper(task))
    return tasks

@router.post("/", status_code=201)
async def create_task(task: TaskCreate):
    new_task = {
        "title": task.title,
        "description": task.description,
        "done": task.done,
        "created_at": datetime.utcnow()
    }
    result = await tasks_collection.insert_one(new_task)
    created_task = await tasks_collection.find_one({"_id": result.inserted_id})
    return task_helper(created_task)

@router.get("/{task_id}")
async def get_task(task_id: str):
    task = await tasks_collection.find_one({"_id": ObjectId(task_id)})
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task_helper(task)

@router.put("/{task_id}")
async def update_task(task_id: str, task: TaskCreate):
    result = await tasks_collection.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": task.dict()}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Task not found")
    updated_task = await tasks_collection.find_one({"_id": ObjectId(task_id)})
    return task_helper(updated_task)

@router.delete("/{task_id}", status_code=204)
async def delete_task(task_id: str):
    result = await tasks_collection.delete_one({"_id": ObjectId(task_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Task not found")
    return None
