import json

# Paths for the input JSON and OpenAPI spec
input_json_path = "engine/master.json"
openapi_file_path = "frontend/openapi.json"

# Load the input JSON containing the module and fields structure
with open(input_json_path, "r") as file:
    modules = json.load(file)

# Load the existing OpenAPI spec file if it exists; otherwise, initialize a new one
try:
    with open(openapi_file_path, "r") as file:
        openapi_structure = json.load(file)
except FileNotFoundError:
    # Initialize the base OpenAPI structure if the file does not exist
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

# Function to update paths and schemas for a given module
def add_module_to_openapi(module, openapi_structure):
    module_name = module["module"]
    path = f"/api/v1/{module_name}/"

    # Add paths for GET and POST
    if path not in openapi_structure["paths"]:
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
                                    "title": f"Response List All {module_name.capitalize()} Api V1 {module_name} Get"
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

    # Add schemas to components if not already present
    schemas = openapi_structure["components"]["schemas"]
    schemas[f"{module_name.capitalize()}Create"] = create_schema
    schemas[f"{module_name.capitalize()}Read"] = read_schema

# Add each module to the OpenAPI structure
for module in modules:
    add_module_to_openapi(module, openapi_structure)

# Write the updated OpenAPI structure back to the file
with open(openapi_file_path, "w") as file:
    json.dump(openapi_structure, file, indent=2)

print(f"Updated OpenAPI spec saved to {openapi_file_path}")
