from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List


employees = [
    {"id": 1, "name": "Alice", "age": 30, "position": "Software Engineer", "salary": 80000},
    {"id": 2, "name": "Bob", "age": 35, "position": "Project Manager", "salary": 90000},
    {"id": 3, "name": "Charlie", "age": 28, "position": "Data Scientist", "salary": 95000}
]