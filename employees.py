from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List
from fastapi import APIRouter, HTTPException
from schema import Employee

employeerouter = APIRouter()

@employeerouter.get("/")
async def root():
    return {"message": "Hello Employees"}

@employeerouter.get("/employees", response_model=List[Employee])
async def get_employees():
    return employees

@employeerouter.get("/employees/{employee_id}", response_model=Employee)
async def get_employee(employee_id: int):
    employee = next((emp for emp in employees if emp.id == employee_id), None)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@employeerouter.post("/employees", response_model=Employee)
async def create_employee(employee: Employee):
    employees.append(employee)
    return employee

@employeerouter.put("/employees/{employee_id}", response_model=Employee)
async def update_employee(employee_id: int, updated_employee: Employee):
    employee = next((emp for emp in employees if emp.id == employee_id), None)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    employees.remove(employee)
    employees.append(updated_employee)
    return updated_employee

@employeerouter.delete("/employees/{employee_id}")
async def delete_employee(employee_id: int):
    employee = next((emp for emp in employees if emp.id == employee_id), None)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    employees.remove(employee)
    return {"message": "Employee deleted successfully"}

@employeerouter.patch("/employees/{employee_id}", response_model=Employee)
async def partial_update_employee(employee_id: int, updated_fields: dict):
    employee = next((emp for emp in employees if emp.id == employee_id), None)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    for key, value in updated_fields.items():
        setattr(employee, key, value)
    return employee