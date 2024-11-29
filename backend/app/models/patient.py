from sqlmodel import SQLModel, Field
from typing import Optional

class PatientBase(SQLModel):
    name: str
    age: int
    gender: str
    contact_information: str

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class PatientUpdate(PatientBase):
    name: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    contact_information: Optional[str] = None
