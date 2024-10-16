from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.models.todo import Todo, TodoCreate
from app.schemas.todo import TodoRead, TodoUpdateSchema
from app.core.database import get_session
from app.services.todo_service import create_todo_service, delete_todo_service, get_todo_service, list_all_todos_service, update_todo_service

router = APIRouter()

@router.post("/", response_model=TodoRead)
def create_todo(todo: TodoCreate, session: Session = Depends(get_session)):
    new_todo = create_todo_service(todo, session)
    return new_todo

@router.get("/{todo_id}", response_model=TodoRead)
def get_todo(todo_id: int, session: Session = Depends(get_session)):
    todo = get_todo_service(todo_id, session)
    return todo

# Update Todo by ID
@router.put("/{todo_id}", response_model=TodoRead)
def update_todo(todo_id: int, todo_data: TodoUpdateSchema, session: Session = Depends(get_session)):
    updated_todo = update_todo_service(todo_id, todo_data, session)
    return updated_todo

# Delete Todo by ID
@router.delete("/{todo_id}", response_model=dict)
def delete_todo(todo_id: int, session: Session = Depends(get_session)):
    delete_todo_service(todo_id, session)
    return {"message": "Todo deleted successfully"}

# List All Todos
@router.get("/", response_model=list[TodoRead])
def list_all_todos(session: Session = Depends(get_session)):
    todos = list_all_todos_service(session)
    return todos