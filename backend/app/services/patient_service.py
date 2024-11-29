from fastapi import HTTPException
from sqlmodel import Session, select
from app.models.patient import Patient, PatientCreate, PatientUpdate

def create_patient_service(patient_data: PatientCreate, session: Session):
    patient = Patient.from_orm(patient_data)
    session.add(patient)
    session.commit()
    session.refresh(patient)
    return patient

def get_patient_service(patient_id: int, session: Session):
    patient = session.get(Patient, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

def update_patient_service(patient_id: int, patient_data: PatientUpdate, session: Session):
    patient = session.get(Patient, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    for key, value in patient_data.dict(exclude_unset=True).items():
        setattr(patient, key, value)
    session.add(patient)
    session.commit()
    session.refresh(patient)
    return patient

def delete_patient_service(patient_id: int, session: Session):
    patient = session.get(Patient, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    session.delete(patient)
    session.commit()

def list_all_patients_service(session: Session):
    patients = session.exec(select(Patient)).all()
    return patients