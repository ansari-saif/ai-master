from pydantic import BaseModel
from typing import Optional

class ModuleCreate(BaseModel):
    title: str
    description: Optional[str] = None

class ModuleRead(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    is_completed: bool

    class Config:
        orm_mode = True

class ModuleUpdateSchema(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None

    class Config:
        orm_mode = True
