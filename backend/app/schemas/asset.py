from pydantic import BaseModel
from typing import Optional

class AssetCreate(BaseModel):
    asset_name: str
    quantity: int
    location: str


class AssetRead(BaseModel):
    id: int
    asset_name: str
    quantity: int
    location: str

    class Config:
        orm_mode = True

class AssetUpdateSchema(BaseModel):
    asset_name: Optional[str] = None
    quantity: Optional[int] = None
    location: Optional[str] = None

    class Config:
        orm_mode = True