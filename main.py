from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from employees import employeerouter
from books import booksrouter
from health import healthrouter
from crud import task_router
from crud import task_router
from contextlib import asynccontextmanager
from database import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    await init_db()
    print("Database connected ✅")
    
    yield
    
    # shutdown (optional)
    print("App shutting down 🔴")

app = FastAPI(
    lifespan=lifespan,
    title="Employee API",
    description="API for managing a collection of employees",
    version="1.0.0"
)
app.include_router(task_router)

app.include_router(employeerouter)
app.include_router(booksrouter)
app.include_router(healthrouter)
app.include_router(task_router)