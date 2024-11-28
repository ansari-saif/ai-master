import json
import re
from openai import OpenAI
import os

# Set up your OpenAI API key (Make sure to replace with your actual API key)
client = OpenAI(api_key="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")

def get_ai_response(prompt):
    """Function to get a response from the AI."""
    try:


        response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # You can change this to another model like gpt-3.5-turbo or gpt-4
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
        return response.choices[0].message.content.strip()  # Extracts the response text
    except Exception as e:
        return f"Error fetching response: {str(e)}"

def write_response_to_file(response):
    """Writes the response content to the specified directory and file."""
    # The response should contain directory path and content. Example: "Directory: /path/to/folder FileName: output.txt Content: <content>"
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
    # Accept a prompt from the user
    prompt = input("Enter the prompt: ")

    # Get response from AI
    response = get_ai_response(prompt)
    print("Response from AI:\n", response)
    file = open("res.txt", "w")
    file.write(response)
    file.close()

    # Write response content to appropriate directory/file
    result = write_response_to_file(response)
    print(result)

if __name__ == "__main__":
    main()
