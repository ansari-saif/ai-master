from pydantic import BaseModel
from typing import Optional

class ModuleCreate(BaseModel):
    title: str
    description: Optional[str] = None

class ModuleRead(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    

    class Config:
        orm_mode = True

class ModuleUpdateSchema(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    

    class Config:
        orm_mode = True
