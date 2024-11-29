from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.models.asset import Asset, AssetCreate
from app.schemas.asset import AssetRead, AssetUpdateSchema
from app.core.database import get_session
from app.services.asset_service import (
    create_asset_service, delete_asset_service, get_asset_service, list_all_asset_service, update_asset_service
)

router = APIRouter()

@router.post("/", response_model=AssetRead, tags=["asset"])
def create_asset(asset: AssetCreate, session: Session = Depends(get_session)):
    new_asset = create_asset_service(asset, session)
    return new_asset

@router.get("/{asset_id}", response_model=AssetRead, tags=["asset"])
def get_asset(asset_id: int, session: Session = Depends(get_session)):
    asset = get_asset_service(asset_id, session)
    return asset

@router.put("/{asset_id}", response_model=AssetRead, tags=["asset"])
def update_asset(asset_id: int, asset_data: AssetUpdateSchema, session: Session = Depends(get_session)):
    updated_asset = update_asset_service(asset_id, asset_data, session)
    return updated_asset

@router.delete("/{asset_id}", response_model=dict, tags=["asset"])
def delete_asset(asset_id: int, session: Session = Depends(get_session)):
    delete_asset_service(asset_id, session)
    return {"message": "Asset deleted successfully"}

@router.get("/", response_model=list[AssetRead], tags=["asset"])
def list_all_asset(session: Session = Depends(get_session)):
    asset = list_all_asset_service(session)
    return asset