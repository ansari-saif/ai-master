from sqlmodel import SQLModel, Field
from typing import Optional

class DoctorBase(SQLModel):
    name: str
    specialty: str
    contact_information: str

class DoctorCreate(DoctorBase):
    pass

class Doctor(DoctorBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class DoctorUpdate(DoctorBase):
    name: Optional[str] = None
    specialty: Optional[str] = None
    contact_information: Optional[str] = None
