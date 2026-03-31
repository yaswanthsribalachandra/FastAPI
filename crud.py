from fastapi import APIRouter, HTTPException, status
from typing import List
from models import Task
from beanie import PydanticObjectId

task_router = APIRouter()


@task_router.get("/tasks", response_model=List[Task])
async def get_all_tasks():
    tasks = await Task.find_all().to_list()
    return tasks

@task_router.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
async def create_task(task: Task):
    await task.insert()
    return task


@task_router.get("/tasks/status/{is_completed}", response_model=List[Task])
async def get_tasks_by_status(is_completed: bool):
    tasks = await Task.find(Task.is_completed == is_completed).to_list()
    if tasks:
        return tasks
    raise HTTPException(status_code=404, detail="No tasks found")


@task_router.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: PydanticObjectId, updated_task: Task):
    task = await Task.get(task_id)
    if task:
        task.title = updated_task.title
        task.is_completed = updated_task.is_completed
        await task.save()
        return task
    raise HTTPException(status_code=404, detail="Task not found")


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
    task = await Task.get(task_id)
    if task:
        await task.delete()
        return {"message": "Task deleted successfully"}
    
    # If not found → error
    raise HTTPException(status_code=404, detail="Task not found")