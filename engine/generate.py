import json
import re
from openai import OpenAI
import os

from backend_generator import BackendGenerator
from frontend_generator import FrontendGenerator
from openapi_file_generator import generat_openapi_file
import subprocess 

# Set up your OpenAI API key (Make sure to replace with your actual API key)
client = OpenAI(api_key="")


def get_ai_response(prompt):
    """Function to get a response from the AI."""
    try:

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            # You can change this to another model like gpt-3.5-turbo or gpt-4
            messages=[
                {
                    "role": "system",
                    "content": [
                        {
                            "type": "text",
                            "text": "You're a senior dev.   just generate the code block itself in json format. [\n    {\n        \"module\": \"module it should be in singular one word\",\n        \"fields\": [\n            {\n                \"name\": \"field_name\",\n                \"type\": \"field_type\"\n            }\n        ]\n    }\n]`"
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt
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
        return response.choices[0].message.content.strip().strip("```json").strip("```")
    except Exception as e:
        return f"Error fetching response: {str(e)}"


def main():
    # Accept a prompt from the user
    with open("engine/prd.txt", "r") as file:
        prompt = file.read()

        # Get response from AI
        response = get_ai_response(prompt)
        file = open("engine/master.json", "w")
        print("master.json file created successfully.")
        file.write(response)
        file.close()
        user_input = input("Review master.json file and feel free to change it. Press Y if you're done (Y/n): ").strip().lower()
        
        if user_input != 'y':
            print("Exiting the code generation process.")
            return
        generat_openapi_file()
        print("OpenAPI file generated successfully.")
        
        print("\nGenerating backend files...")
        BackendGenerator(client)
        print("Backend files generated successfully.")
        
        subprocess.run(["npm", "run", "generate-client"], cwd="frontend", check=True)
        print("Client generated successfully.")
        
        print("\nGenerating frontend files...")
        FrontendGenerator(client)
        print("Frontend files generated successfully.")
        
        print("\nStarting backend server...")
        subprocess.run(["uvicorn", "app.main:app", "--reload"], cwd="backend", check=True)
        print("Backend server started successfully.")
        
        if os.path.exists("engine/master.json"):
            os.remove("engine/master.json")
            print("engine/master.json file deleted successfully.")
        else:
            print("engine/master.json file does not exist.")

if __name__ == "__main__":
    main()

