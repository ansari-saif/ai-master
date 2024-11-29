from fastapi import HTTPException
from sqlmodel import Session, select
from app.models.doctor import Doctor, DoctorCreate, DoctorUpdate

def create_doctor_service(doctor_data: DoctorCreate, session: Session):
    doctor = Doctor.from_orm(doctor_data)
    session.add(doctor)
    session.commit()
    session.refresh(doctor)
    return doctor

def get_doctor_service(doctor_id: int, session: Session):
    doctor = session.get(Doctor, doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor

def update_doctor_service(doctor_id: int, doctor_data: DoctorUpdate, session: Session):
    doctor = session.get(Doctor, doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    for key, value in doctor_data.dict(exclude_unset=True).items():
        setattr(doctor, key, value)
    session.add(doctor)
    session.commit()
    session.refresh(doctor)
    return doctor

def delete_doctor_service(doctor_id: int, session: Session):
    doctor = session.get(Doctor, doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    session.delete(doctor)
    session.commit()

def list_all_doctor_service(session: Session):
    doctor = session.exec(select(Doctor)).all()
    return doctor