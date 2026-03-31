from pydantic import BaseModel
from beanie import Document
from datetime import datetime
from pydantic import Field

class Employee(BaseModel):
    id: int
    name: str
    age: int
    position: str
    salary : int


class Task(Document):
    title: str
    is_completed: bool = False

    class Settings:
        name = "task"