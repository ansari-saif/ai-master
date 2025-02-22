from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.models.module import Module, ModuleCreate
from app.schemas.module import ModuleRead, ModuleUpdateSchema
from app.core.database import get_session
from app.services.module_service import (
    create_module_service, delete_module_service, get_module_service, list_all_module_service, update_module_service
)

router = APIRouter()

@router.post("/", response_model=ModuleRead, tags=["module"])
def create_module(module: ModuleCreate, session: Session = Depends(get_session)):
    new_module = create_module_service(module, session)
    return new_module

@router.get("/{module_id}", response_model=ModuleRead, tags=["module"])
def get_module(module_id: int, session: Session = Depends(get_session)):
    module = get_module_service(module_id, session)
    return module

@router.put("/{module_id}", response_model=ModuleRead, tags=["module"])
def update_module(module_id: int, module_data: ModuleUpdateSchema, session: Session = Depends(get_session)):
    updated_module = update_module_service(module_id, module_data, session)
    return updated_module

@router.delete("/{module_id}", response_model=dict, tags=["module"])
def delete_module(module_id: int, session: Session = Depends(get_session)):
    delete_module_service(module_id, session)
    return {"message": "Module deleted successfully"}

@router.get("/", response_model=list[ModuleRead], tags=["module"])
def list_all_module(session: Session = Depends(get_session)):
    module = list_all_module_service(session)
    return module
