from beanie import Document
from datetime import datetime
from pydantic import Field

class Task(Document):
    title: str
    is_completed: bool = False

    class Settings:
        name = "task"