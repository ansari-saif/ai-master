from fastapi import HTTPException
from sqlmodel import Session, select
from app.models.asset import Asset, AssetCreate, AssetUpdate

def create_asset_service(asset_data: AssetCreate, session: Session):
    asset = Asset.from_orm(asset_data)
    session.add(asset)
    session.commit()
    session.refresh(asset)
    return asset

def get_asset_service(asset_id: int, session: Session):
    asset = session.get(Asset, asset_id)
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    return asset

def update_asset_service(asset_id: int, asset_data: AssetUpdate, session: Session):
    asset = session.get(Asset, asset_id)
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    for key, value in asset_data.dict(exclude_unset=True).items():
        setattr(asset, key, value)
    session.add(asset)
    session.commit()
    session.refresh(asset)
    return asset

def delete_asset_service(asset_id: int, session: Session):
    asset = session.get(Asset, asset_id)
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    session.delete(asset)
    session.commit()

def list_all_assets_service(session: Session):
    assets = session.exec(select(Asset)).all()
    return assets
