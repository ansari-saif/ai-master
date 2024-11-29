from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.models.patient import Patient, PatientCreate
from app.schemas.patient import PatientRead, PatientUpdateSchema
from app.core.database import get_session
from app.services.patient_service import (
    create_patient_service, delete_patient_service, get_patient_service, list_all_patient_service, update_patient_service
)

router = APIRouter()

@router.post("/", response_model=PatientRead, tags=["patient"])
def create_patient(patient: PatientCreate, session: Session = Depends(get_session)):
    new_patient = create_patient_service(patient, session)
    return new_patient

@router.get("/{patient_id}", response_model=PatientRead, tags=["patient"])
def get_patient(patient_id: int, session: Session = Depends(get_session)):
    patient = get_patient_service(patient_id, session)
    return patient

@router.put("/{patient_id}", response_model=PatientRead, tags=["patient"])
def update_patient(patient_id: int, patient_data: PatientUpdateSchema, session: Session = Depends(get_session)):
    updated_patient = update_patient_service(patient_id, patient_data, session)
    return updated_patient

@router.delete("/{patient_id}", response_model=dict, tags=["patient"])
def delete_patient(patient_id: int, session: Session = Depends(get_session)):
    delete_patient_service(patient_id, session)
    return {"message": "Patient deleted successfully"}

@router.get("/", response_model=list[PatientRead], tags=["patient"])
def list_all_patient(session: Session = Depends(get_session)):
    patient = list_all_patient_service(session)
    return patient