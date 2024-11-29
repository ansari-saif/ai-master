from pydantic import BaseModel
from typing import Optional

class DoctorCreate(BaseModel):
    name: str
    specialty: str
    contact_information: str

class DoctorRead(BaseModel):
    id: int
    name: str
    specialty: str
    contact_information: str

    class Config:
        orm_mode = True

class DoctorUpdateSchema(BaseModel):
    name: Optional[str] = None
    specialty: Optional[str] = None
    contact_information: Optional[str] = None

    class Config:
        orm_mode = True
