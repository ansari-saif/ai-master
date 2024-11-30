import json
import re
from openai import OpenAI
import os

from engine.backend_generator import BackendGenerator
from engine.frontend_generator import FrontendGenerator
from engine.openapi_file_generator import generat_openapi_file
import subprocess 

# Set up your OpenAI API key (Make sure to replace with your actual API key)
client = OpenAI(api_key="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")


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
                            "text": "You're a senior dev.   just generate the code block itself in json format. [\n    {\n        \"module\": \"module name in snake case\",\n        \"fields\": [\n            {\n                \"name\": \"field_name\",\n                \"type\": \"field_type\"\n            }\n        ]\n    }\n]`"
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
        print("Response from AI:\n", response)
        file = open("engine/master.json", "w")
        file.write(response)
        file.close()
        user_input = input("Review master.json file and feel free to change it. Press Y if you're done (Y/n): ").strip().lower()
        if user_input != 'Y':
            print("Exiting the code generation process.")
            return
        generat_openapi_file()
        print("OpenAPI file generated successfully.")
        BackendGenerator(client)
        print("Backend files generated successfully.")
        subprocess.run(["npm", "run", "generate-client"], cwd="frontend", check=True)
        print("Client generated successfully.")
        FrontendGenerator(client)
        print("Frontend files generated successfully.")
      

if __name__ == "__main__":
    main()

