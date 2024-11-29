import json

# Input JSON (module and fields structure)
with open("engine/master.json", "r") as file:
    input_json = file.read()

# Parse the input JSON
modules = json.loads(input_json)

# Initialize the base OpenAPI structure
openapi_structure = {
    "openapi": "3.1.0",
    "info": {
        "title": "Cogent Ai",
        "version": "0.1.0"
    },
    "servers": [
        {
            "url": "http://localhost:8000",
            "description": "Local development server"
        }
    ],
    "paths": {},
    "components": {
        "schemas": {}
    }
}

# Loop through each module in the input
for module in modules:
    # Define paths for each module
    module_name = module["module"]
    path = f"/api/v1/{module_name}/"
    openapi_structure["paths"][path] = {
        "get": {
            "tags": [module_name],
            "summary": f"List All {module_name.capitalize()}",
            "operationId": f"list_all_{module_name}_api_v1_{module_name}__get",
            "responses": {
                "200": {
                    "description": "Successful Response",
                    "content": {
                        "application/json": {
                            "schema": {
                                "items": {
                                    "$ref": f"#/components/schemas/{module_name.capitalize()}Read"
                                },
                                "type": "array",
                                "title": f"Response List All {module_name.capitalize()} Api V1 {module_name}  Get"
                            }
                        }
                    }
                }
            }
        },
        "post": {
            "tags": [module_name],
            "summary": f"Create {module_name.capitalize()}",
            "operationId": f"create_{module_name}_api_v1_{module_name}__post",
            "requestBody": {
                "content": {
                    "application/json": {
                        "schema": {
                            "$ref": f"#/components/schemas/{module_name.capitalize()}Create"
                        }
                    }
                },
                "required": True
            },
            "responses": {
                "200": {
                    "description": "Successful Response",
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": f"#/components/schemas/{module_name.capitalize()}Read"
                            }
                        }
                    }
                }
            }
        }
    }

    # Initialize schemas for Create and Read
    create_schema = {
        "properties": {},
        "type": "object",
        "required": [],
        "title": f"{module_name.capitalize()}Create"
    }
    read_schema = {
        "properties": {
            "id": {
                "type": "integer",
                "title": "Id"
            }
        },
        "type": "object",
        "required": ["id"],
        "title": f"{module_name.capitalize()}Read"
    }

    # Add fields to the schemas
    for field in module["fields"]:
        field_name = field["name"]
        field_type = field["type"]

        # Update Create schema
        create_schema["properties"][field_name] = {
            "type": field_type,
            "title": field_name.capitalize()
        }
        create_schema["required"].append(field_name)

        # Update Read schema
        read_schema["properties"][field_name] = {
            "type": field_type,
            "title": field_name.capitalize()
        }
        read_schema["required"].append(field_name)

    # Add schemas to components
    openapi_structure["components"]["schemas"][f"{module_name.capitalize()}Create"] = create_schema
    openapi_structure["components"]["schemas"][f"{module_name.capitalize()}Read"] = read_schema

# Print the converted OpenAPI structure as a JSON string
with open("frontend/openapi.json", "w") as file:
    json.dump(openapi_structure, file, indent=2)
