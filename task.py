from fastapi import APIRouter, HTTPException, status
from typing import List
from models import Task
from beanie import PydanticObjectId

task_router = APIRouter()

@task_router.get("/tasks", response_model=List[Task])
async def get_all_tasks():
    return await Task.find_all().to_list()


@task_router.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
async def create_task(task: Task):
    await task.insert()
    return task


@task_router.patch("/tasks/{task_id}", response_model=Task)
async def partial_update_task(task_id: PydanticObjectId, task_data: dict):
    task = await Task.get(task_id)
    if task:
        for key, value in task_data.items():
            setattr(task, key, value)
        await task.save()
        return task
    raise HTTPException(status_code=404, detail="Task not found")


@task_router.delete("/tasks/{task_id}")
async def delete_task(task_id: PydanticObjectId):
    task = await Task.get(task_id)   # ✅ FIXED
    if task:
        await task.delete()
        return {"message": "Task deleted successfully"}
    
    raise HTTPException(status_code=404, detail="Task not found")