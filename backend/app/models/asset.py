from sqlmodel import SQLModel, Field
from typing import Optional

class AssetBase(SQLModel):
    asset_name: str
    quantity: int
    location: str

class AssetCreate(AssetBase):
    pass

class Asset(AssetBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class AssetUpdate(AssetBase):
    asset_name: Optional[str] = None
    quantity: Optional[int] = None
    location: Optional[str] = None