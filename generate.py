from openai import OpenAI
import os

# Set up your OpenAI API key (Make sure to replace with your actual API key)
client = OpenAI(api_key="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")

def get_ai_response(prompt):
    """Function to get a response from the AI."""
    try:


        response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
            "role": "system",
            "content": [
               {
          "type": "text",
          "text": "You're a senior dev. Don't explain the code, just generate the code block itself .\n\nexample \n```dir/hello.py\n# code here\n```"
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
        max_tokens=500
        )
        return response.choices[0].message.content.strip()  # Extracts the response text
    except Exception as e:
        return f"Error fetching response: {str(e)}"

def write_response_to_file(response):
    """Writes the response content to the specified directory and file."""
    # The response should contain directory path and content. Example: "Directory: /path/to/folder FileName: output.txt Content: <content>"
    try:
        # Extract directory, filename, and content from response
        lines = response.split("\n")
        directory = lines[0].split("Directory:")[1].strip()
        filename = lines[1].split("FileName:")[1].strip()
        content = "\n".join(lines[2:]).strip()

        # Ensure the directory exists
        os.makedirs(directory, exist_ok=True)

        # Define file path
        file_path = os.path.join(directory, filename)

        # Write content to the file
        with open(file_path, 'w') as file:
            file.write(content)
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
    # result = write_response_to_file(response)
    # print(result)

if __name__ == "__main__":
    main()
