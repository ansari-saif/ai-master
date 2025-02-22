from fastapi import HTTPException
from sqlmodel import Session, select
from app.models.module import Module, ModuleCreate, ModuleUpdate

def create_module_service(module_data: ModuleCreate, session: Session):
    module = Module.from_orm(module_data)
    session.add(module)
    session.commit()
    session.refresh(module)
    return module

def get_module_service(module_id: int, session: Session):
    module = session.get(Module, module_id)
    if not module:
        raise HTTPException(status_code=404, detail="Module not found")
    return module

# Update Module service
def update_module_service(module_id: int, module_data: ModuleUpdate, session: Session):
    module = session.get(Module, module_id)
    if not module:
        raise HTTPException(status_code=404, detail="Module not found")
    for key, value in module_data.dict(exclude_unset=True).items():
        setattr(module, key, value)
    session.add(module)
    session.commit()
    session.refresh(module)
    return module

# Delete Module service
def delete_module_service(module_id: int, session: Session):
    module = session.get(Module, module_id)
    if not module:
        raise HTTPException(status_code=404, detail="Module not found")
    session.delete(module)
    session.commit()

# List All module service
def list_all_module_service(session: Session):
    module = session.exec(select(Module)).all()
    return module
