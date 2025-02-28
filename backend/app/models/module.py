from sqlmodel import SQLModel, Field
from typing import Optional

class ModuleBase(SQLModel):
    title: str
    description: Optional[str] = None
    is_completed: bool = False

class ModuleCreate(ModuleBase):
    pass

class Module(ModuleBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class ModuleUpdate(ModuleBase):
    title: Optional[str] = None
    description: Optional[str] = None
