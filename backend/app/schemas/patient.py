from pydantic import BaseModel
from typing import Optional

class PatientCreate(BaseModel):
    name: str
    age: int
    gender: str
    contact_information: str

class PatientRead(BaseModel):
    id: int
    name: str
    age: int
    gender: str
    contact_information: str

    class Config:
        orm_mode = True

class PatientUpdateSchema(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    contact_information: Optional[str] = None

    class Config:
        orm_mode = True