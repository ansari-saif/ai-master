import json

import os

class BackendGenerator:
    def __init__(self, client):
        self.client = client
        self.main()
    def get_ai_response(self, json_data):
        """Function to get a response from the AI."""
        module = json_data["module"]

        try:
            response = self.client.chat.completions.create(
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
                f"\nAdd `{module}` module. here is the fields \n\"\"\"\n {json_data} \n\"\"\"\n\n"
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
                "|   |   |   module.py\n"
                "|   |   schemas\n"
                "|   |   |   __init__.py\n"
                "|   |   |   module.py\n"
                "|   |   api\n"
                "|   |   |   v1\n"
                "|   |   |   |   __init__.py\n"
                "|   |   |   |   routes\n"
                "|   |   |   |   |   module.py\n"
                "|   |   |   |   |   __init__.py\n"
                "|   |   |   __init__.py\n"
                "|   |   main.py\n"
                "|   |   services\n"
                "|   |   |   __init__.py\n"
                "|   |   |   module_service.py\n"
                "|   requirements.txt\n"
                "|   Dockerfile\n"
                "|   test.db\n"
                "\"\"\"\n"
                "you've to follow current code structure and you've to create models, schema, services and routes \n\n"
                "here is one sample\n"
                "backend/app/api/v1/routes/module.py\n\n"
                "```\n"
                "from fastapi import APIRouter, Depends, HTTPException\n"
                "from sqlmodel import Session, select\n"
                "from app.models.module import Module, ModuleCreate\n"
                "from app.schemas.module import ModuleRead, ModuleUpdateSchema\n"
                "from app.core.database import get_session\n"
                "from app.services.module_service import (\n"
                "    create_module_service, delete_module_service, get_module_service, list_all_module_service, update_module_service\n"
                ")\n\n"
                "router = APIRouter()\n\n"
                "@router.post(\"/\", response_model=ModuleRead, tags=[\"module\"])\n"
                "def create_module(module: ModuleCreate, session: Session = Depends(get_session)):\n"
                "    new_module = create_module_service(module, session)\n"
                "    return new_module\n\n"
                "@router.get(\"/{module_id}\", response_model=ModuleRead, tags=[\"module\"])\n"
                "def get_module(module_id: int, session: Session = Depends(get_session)):\n"
                "    module = get_module_service(module_id, session)\n"
                "    return module\n\n"
                "# Update Module by ID\n"
                "@router.put(\"/{module_id}\", response_model=ModuleRead, tags=[\"module\"])\n"
                "def update_module(module_id: int, module_data: ModuleUpdateSchema, session: Session = Depends(get_session)):\n"
                "    updated_module = update_module_service(module_id, module_data, session)\n"
                "    return updated_module\n\n"
                "# Delete Module by ID\n"
                "@router.delete(\"/{module_id}\", response_model=dict, tags=[\"module\"])\n"
                "def delete_module(module_id: int, session: Session = Depends(get_session)):\n"
                "    delete_module_service(module_id, session)\n"
                "    return {\"message\": \"Module deleted successfully\"}\n\n"
                "# List All module\n"
                "@router.get(\"/\", response_model=list[ModuleRead], tags=[\"module\"])\n"
                "def list_all_module(session: Session = Depends(get_session)):\n"
                "    module = list_all_module_service(session)\n"
                "    return module\n"
                "```\n"
                "\n"
                "Here is the model, schema, and service files for the 'Module' functionality:\n\n"
                "```python\n"
                "backend/app/schemas/module.py\n"
                "from pydantic import BaseModel\n"
                "from typing import Optional\n\n"
                "class ModuleCreate(BaseModel):\n"
                "    title: str\n"
                "    description: Optional[str] = None\n\n"
                "class ModuleRead(BaseModel):\n"
                "    id: int\n"
                "    title: str\n"
                "    description: Optional[str] = None\n"
                "    is_completed: bool\n\n"
                "    class Config:\n"
                "        orm_mode = True\n\n"
                "class ModuleUpdateSchema(BaseModel):\n"
                "    title: Optional[str] = None\n"
                "    description: Optional[str] = None\n"
                "    is_completed: Optional[bool] = None\n\n"
                "    class Config:\n"
                "        orm_mode = True\n"
                "```\n"
                "\n"
                "```python\n"
                "backend/app/models/module.py\n"
                "from sqlmodel import SQLModel, Field\n"
                "from typing import Optional\n\n"
                "class ModuleBase(SQLModel):\n"
                "    title: str\n"
                "    description: Optional[str] = None\n"
                "    is_completed: bool = False\n\n"
                "class ModuleCreate(ModuleBase):\n"
                "    pass\n\n"
                "class Module(ModuleBase, table=True):\n"
                "    id: Optional[int] = Field(default=None, primary_key=True)\n\n"
                "class ModuleUpdate(ModuleBase):\n"
                "    title: Optional[str] = None\n"
                "    description: Optional[str] = None\n"
                "    is_completed: Optional[bool] = None\n"
                "```\n"
                "\n"
                "```python\n"
                "backend/app/services/module_service.py\n"
                "from fastapi import HTTPException\n"
                "from sqlmodel import Session, select\n"
                "from app.models.module import Module, ModuleCreate, ModuleUpdate\n\n"
                "def create_module_service(module_data: ModuleCreate, session: Session):\n"
                "    module = Module.from_orm(module_data)\n"
                "    session.add(module)\n"
                "    session.commit()\n"
                "    session.refresh(module)\n"
                "    return module\n\n"
                "def get_module_service(module_id: int, session: Session):\n"
                "    module = session.get(Module, module_id)\n"
                "    if not module:\n"
                "        raise HTTPException(status_code=404, detail=\"Module not found\")\n"
                "    return module\n\n"
                "# Update Module service\n"
                "def update_module_service(module_id: int, module_data: ModuleUpdate, session: Session):\n"
                "    module = session.get(Module, module_id)\n"
                "    if not module:\n"
                "        raise HTTPException(status_code=404, detail=\"Module not found\")\n"
                "    for key, value in module_data.dict(exclude_unset=True).items():\n"
                "        setattr(module, key, value)\n"
                "    session.add(module)\n"
                "    session.commit()\n"
                "    session.refresh(module)\n"
                "    return module\n\n"
                "# Delete Module service\n"
                "def delete_module_service(module_id: int, session: Session):\n"
                "    module = session.get(Module, module_id)\n"
                "    if not module:\n"
                "        raise HTTPException(status_code=404, detail=\"Module not found\")\n"
                "    session.delete(module)\n"
                "    session.commit()\n\n"
                "# List All module service\n"
                "def list_all_module_service(session: Session):\n"
                "    module = session.exec(select(Module)).all()\n"
                "    return module\n"
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


    def get_ai_response2(self, json_item):
        module = json_item["module"]
        """Function to get a response from the AI."""
        try:
            main_file_path = 'backend/app/main.py'
            with open(main_file_path, 'r') as file:
                main_file_content = file.read()
            response = self.client.chat.completions.create(
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
                f"add import and router for `{module}` module in this file \n\n"
                        
                "```python\n"
                f"{main_file_path}\n"
                f"{main_file_content}\n"
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


    def write_response_to_file(self, response):
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


    def main(self):
        # Read the master.json file to get the JSON data
        with open('engine/master.json', 'r') as file:
            json_data = json.loads(file.read())
            for json_item in json_data:
                response = self.get_ai_response(json_item)
                result = self.write_response_to_file(response)
                response = self.get_ai_response2(json_item)
                result = self.write_response_to_file(response)
                print(json_item["module"], "done")


