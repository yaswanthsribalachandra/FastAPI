from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List
from database import employees
from fastapi import APIRouter, HTTPException

app = FastAPI(
    title="Health API",
    description="API for managing health-related data",
    version="1.0.0"
)

class HealthCheckResponse(BaseModel):
    user:str
    age:int
    condition: str

patients = [
    {"id": 1, "name": "Alice", "age": 30, "condition": "Healthy"},
    {"id": 2, "name": "Bob", "age": 35, "condition": "Diabetes"},
    {"id": 3, "name": "Charlie", "age": 28, "condition": "Hypertension"}
]

healthrouter = APIRouter()

@healthrouter.get("/patients", response_model=List[HealthCheckResponse])
async def get_patients():
    return [HealthCheckResponse(patient) for patient in patients]

@healthrouter.get("/patients/{patient_id}", response_model=HealthCheckResponse)
async def get_patient(patient_id: int):
    patient = next((pat for pat in patients if pat["id"] == patient_id), None)
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return HealthCheckResponse(patient)

@healthrouter.post("/patients", response_model=HealthCheckResponse)
async def create_patient(patient: HealthCheckResponse):
    patients.append(patient.dict())
    return patient

@healthrouter.put("/patients/{patient_id}", response_model=HealthCheckResponse)
async def update_patient(patient_id: int, updated_patient: HealthCheckResponse):
    patient = next((pat for pat in patients if pat["id"] == patient_id), None)
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    patients.remove(patient)
    patients.append(updated_patient.dict())
    return updated_patient

@healthrouter.delete("/patients/{patient_id}")
async def delete_patient(patient_id: int):
    patient = next((pat for pat in patients if pat["id"] == patient_id), None)
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    patients.remove(patient)
    return {"message": "Patient deleted successfully"}

@healthrouter.patch("/patients/{patient_id}", response_model=HealthCheckResponse)
async def partial_update_patient(patient_id: int, updated_fields: dict):
    patient = next((pat for pat in patients if pat["id"] == patient_id), None)
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    for key, value in updated_fields.items():
        setattr(patient, key, value)
    return HealthCheckResponse(**patient)