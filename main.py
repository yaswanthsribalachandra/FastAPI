from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from employees import employeerouter
from books import booksrouter
from health import healthrouter


app = FastAPI(
    title="Employee API",
    description="API for managing a collection of employees",
    version="1.0.0"
)

app.include_router(employeerouter)
app.include_router(booksrouter)
app.include_router(healthrouter)