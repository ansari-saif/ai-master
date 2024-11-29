import json
import re
from openai import OpenAI
import os

# Set up your OpenAI API key (Make sure to replace with your actual API key)
client = OpenAI(api_key="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")


def get_ai_response(json_data):
    """Function to get a response from the AI."""
    try:

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": [
                        {
                            "type": "text",
                            "text": "You're a senior dev. Don't explain the code, just generate the code block itself in json format.\n\nexample \n```[{\n\"file_path\":\"path of the file\",\n\"file_content\":\"code of the file\",\n}]```"
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": (
            f"\ncreate crud apis in fastapi for this \n\"\"\"\n {json_data} \n\"\"\"\n\n"
            "here is the current file directory\n\n"
            "\"\"\"\n"
            "backend\n"
            "|   app\n"
            "|   |   core\n"
            "|   |   |   config.py\n"
            "|   |   |   database.py\n"
            "|   |   |   __init__.py\n"
            "|   |   models\n"
            "|   |   |   __init__.py\n"
            "|   |   |   todo.py\n"
            "|   |   schemas\n"
            "|   |   |   __init__.py\n"
            "|   |   |   todo.py\n"
            "|   |   api\n"
            "|   |   |   v1\n"
            "|   |   |   |   __init__.py\n"
            "|   |   |   |   routes\n"
            "|   |   |   |   |   todo.py\n"
            "|   |   |   |   |   __init__.py\n"
            "|   |   |   __init__.py\n"
            "|   |   main.py\n"
            "|   |   services\n"
            "|   |   |   __init__.py\n"
            "|   |   |   todo_service.py\n"
            "|   requirements.txt\n"
            "|   Dockerfile\n"
            "|   test.db\n"
            "\"\"\"\n"
            "you've to follow current code structure and you've to create models, schema, services and routes \n\n"
            "here is one sample\n"
            "backend/app/api/v1/routes/todo.py\n\n"
            "```\n"
            "from fastapi import APIRouter, Depends, HTTPException\n"
            "from sqlmodel import Session, select\n"
            "from app.models.todo import Todo, TodoCreate\n"
            "from app.schemas.todo import TodoRead, TodoUpdateSchema\n"
            "from app.core.database import get_session\n"
            "from app.services.todo_service import (\n"
            "    create_todo_service, delete_todo_service, get_todo_service, list_all_todo_service, update_todo_service\n"
            ")\n\n"
            "router = APIRouter()\n\n"
            "@router.post(\"/\", response_model=TodoRead, tags=[\"todo\"])\n"
            "def create_todo(todo: TodoCreate, session: Session = Depends(get_session)):\n"
            "    new_todo = create_todo_service(todo, session)\n"
            "    return new_todo\n\n"
            "@router.get(\"/{todo_id}\", response_model=TodoRead, tags=[\"todo\"])\n"
            "def get_todo(todo_id: int, session: Session = Depends(get_session)):\n"
            "    todo = get_todo_service(todo_id, session)\n"
            "    return todo\n\n"
            "# Update Todo by ID\n"
            "@router.put(\"/{todo_id}\", response_model=TodoRead, tags=[\"todo\"])\n"
            "def update_todo(todo_id: int, todo_data: TodoUpdateSchema, session: Session = Depends(get_session)):\n"
            "    updated_todo = update_todo_service(todo_id, todo_data, session)\n"
            "    return updated_todo\n\n"
            "# Delete Todo by ID\n"
            "@router.delete(\"/{todo_id}\", response_model=dict, tags=[\"todo\"])\n"
            "def delete_todo(todo_id: int, session: Session = Depends(get_session)):\n"
            "    delete_todo_service(todo_id, session)\n"
            "    return {\"message\": \"Todo deleted successfully\"}\n\n"
            "# List All todo\n"
            "@router.get(\"/\", response_model=list[TodoRead], tags=[\"todo\"])\n"
            "def list_all_todo(session: Session = Depends(get_session)):\n"
            "    todo = list_all_todo_service(session)\n"
            "    return todo\n"
            "```\n"
            "\n"
            "Here is the model, schema, and service files for the 'Todo' functionality:\n\n"
            "```python\n"
            "backend/app/schemas/todo.py\n"
            "from pydantic import BaseModel\n"
            "from typing import Optional\n\n"
            "class TodoCreate(BaseModel):\n"
            "    title: str\n"
            "    description: Optional[str] = None\n\n"
            "class TodoRead(BaseModel):\n"
            "    id: int\n"
            "    title: str\n"
            "    description: Optional[str] = None\n"
            "    is_completed: bool\n\n"
            "    class Config:\n"
            "        orm_mode = True\n\n"
            "class TodoUpdateSchema(BaseModel):\n"
            "    title: Optional[str] = None\n"
            "    description: Optional[str] = None\n"
            "    is_completed: Optional[bool] = None\n\n"
            "    class Config:\n"
            "        orm_mode = True\n"
            "```\n"
            "\n"
            "```python\n"
            "backend/app/models/todo.py\n"
            "from sqlmodel import SQLModel, Field\n"
            "from typing import Optional\n\n"
            "class TodoBase(SQLModel):\n"
            "    title: str\n"
            "    description: Optional[str] = None\n"
            "    is_completed: bool = False\n\n"
            "class TodoCreate(TodoBase):\n"
            "    pass\n\n"
            "class Todo(TodoBase, table=True):\n"
            "    id: Optional[int] = Field(default=None, primary_key=True)\n\n"
            "class TodoUpdate(TodoBase):\n"
            "    title: Optional[str] = None\n"
            "    description: Optional[str] = None\n"
            "    is_completed: Optional[bool] = None\n"
            "```\n"
            "\n"
            "```python\n"
            "backend/app/services/todo_service.py\n"
            "from fastapi import HTTPException\n"
            "from sqlmodel import Session, select\n"
            "from app.models.todo import Todo, TodoCreate, TodoUpdate\n\n"
            "def create_todo_service(todo_data: TodoCreate, session: Session):\n"
            "    todo = Todo.from_orm(todo_data)\n"
            "    session.add(todo)\n"
            "    session.commit()\n"
            "    session.refresh(todo)\n"
            "    return todo\n\n"
            "def get_todo_service(todo_id: int, session: Session):\n"
            "    todo = session.get(Todo, todo_id)\n"
            "    if not todo:\n"
            "        raise HTTPException(status_code=404, detail=\"Todo not found\")\n"
            "    return todo\n\n"
            "# Update Todo service\n"
            "def update_todo_service(todo_id: int, todo_data: TodoUpdate, session: Session):\n"
            "    todo = session.get(Todo, todo_id)\n"
            "    if not todo:\n"
            "        raise HTTPException(status_code=404, detail=\"Todo not found\")\n"
            "    for key, value in todo_data.dict(exclude_unset=True).items():\n"
            "        setattr(todo, key, value)\n"
            "    session.add(todo)\n"
            "    session.commit()\n"
            "    session.refresh(todo)\n"
            "    return todo\n\n"
            "# Delete Todo service\n"
            "def delete_todo_service(todo_id: int, session: Session):\n"
            "    todo = session.get(Todo, todo_id)\n"
            "    if not todo:\n"
            "        raise HTTPException(status_code=404, detail=\"Todo not found\")\n"
            "    session.delete(todo)\n"
            "    session.commit()\n\n"
            "# List All todo service\n"
            "def list_all_todo_service(session: Session):\n"
            "    todo = session.exec(select(Todo)).all()\n"
            "    return todo\n"
            "```\n"
        )
                        }
                    ]
                },

            ],
            response_format={
                "type": "text"
            },
            temperature=0,
            max_tokens=2048,
        )
        # Extracts the response text
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error fetching response: {str(e)}"


def write_response_to_file(response):
    """Writes the response content to the specified directory and file."""
    # The response should contain directory path and content. Example:
    # "Directory: /path/to/folder FileName: output.txt Content: <content>"
    try:
        # Extract directory, filename, and content from response
        data_list = json.loads(response.strip("```json").strip("```"))
        for file in data_list:
            file_path = file["file_path"]
            os.makedirs(os.path.dirname(file_path), exist_ok=True)

            with open(file_path, 'w') as f:
                f.write(file["file_content"])
        return f"Content successfully written to {file_path}"
    except Exception as e:
        return f"Error writing to file: {str(e)}"


def main():
    # Read the master.json file to get the JSON data
    with open('engine/master.json', 'r') as file:
        json_data = json.loads(file.read())
        for json_item in json_data:
            response = get_ai_response(json_item)
        

            # Write response content to appropriate directory/file
            result = write_response_to_file(response)
            print(json_item["module"], "done")


if __name__ == "__main__":
    main()
