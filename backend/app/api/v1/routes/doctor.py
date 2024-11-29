from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.models.doctor import Doctor, DoctorCreate
from app.schemas.doctor import DoctorRead, DoctorUpdateSchema
from app.core.database import get_session
from app.services.doctor_service import (
    create_doctor_service, delete_doctor_service, get_doctor_service, list_all_doctor_service, update_doctor_service
)

router = APIRouter()

@router.post("/", response_model=DoctorRead, tags=["doctor"])
def create_doctor(doctor: DoctorCreate, session: Session = Depends(get_session)):
    new_doctor = create_doctor_service(doctor, session)
    return new_doctor

@router.get("/{doctor_id}", response_model=DoctorRead, tags=["doctor"])
def get_doctor(doctor_id: int, session: Session = Depends(get_session)):
    doctor = get_doctor_service(doctor_id, session)
    return doctor

# Update Doctor by ID
@router.put("/{doctor_id}", response_model=DoctorRead, tags=["doctor"])
def update_doctor(doctor_id: int, doctor_data: DoctorUpdateSchema, session: Session = Depends(get_session)):
    updated_doctor = update_doctor_service(doctor_id, doctor_data, session)
    return updated_doctor

# Delete Doctor by ID
@router.delete("/{doctor_id}", response_model=dict, tags=["doctor"])
def delete_doctor(doctor_id: int, session: Session = Depends(get_session)):
    delete_doctor_service(doctor_id, session)
    return {"message": "Doctor deleted successfully"}

# List All doctor
@router.get("/", response_model=list[DoctorRead], tags=["doctor"])
def list_all_doctor(session: Session = Depends(get_session)):
    doctor = list_all_doctor_service(session)
    return doctor
