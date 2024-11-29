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

    # Create schemas for each module
    for field in module["fields"]:
        field_name = field["name"]
        field_type = field["type"]

        # Schema for Create and Read
        openapi_structure["components"]["schemas"][f"{module_name.capitalize()}Create"] = {
            "properties": {
                field_name: {
                    "type": field_type,
                    "title": field_name.capitalize()
                }
            },
            "type": "object",
            "required": [field_name],
            "title": f"{module_name.capitalize()}Create"
        }

        openapi_structure["components"]["schemas"][f"{module_name.capitalize()}Read"] = {
            "properties": {
                "id": {
                    "type": "integer",
                    "title": "Id"
                },
                field_name: {
                    "type": field_type,
                    "title": field_name.capitalize()
                }
            },
            "type": "object",
            "required": ["id", field_name],
            "title": f"{module_name.capitalize()}Read"
        }

# Print the converted OpenAPI structure as a JSON string
with open("frontend/openapi.json", "w") as file:
    json.dump(openapi_structure, file, indent=2)
