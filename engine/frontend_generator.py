import json
import os

def services_list(word):
    return json.dumps([
        f"listAll{word.capitalize()}ApiV1{word.capitalize()}Get",
        f"create{word.capitalize()}ApiV1{word.capitalize()}Post",
        f"get{word.capitalize()}ApiV1{word.capitalize()}IdGet",
        f"update{word.capitalize()}ApiV1{word.capitalize()}IdPut",
        f"delete{word.capitalize()}ApiV1{word.capitalize()}IdDelete",
    ])

class FrontendGenerator:
    def __init__(self, client):
        self.client = client
        self.main()
        
    def get_ai_response(self, json_item):
        module = json_item["module"]
        json_structure = json_item["fields"]
        """Function to get a response from the AI."""
        try:
            TodoItem = 'frontend/src/components/TodoItem.tsx'
            with open(TodoItem, 'r') as file:
                TodoItemContent = file.read()
                
            AddTodoFormContent = 'frontend/src/components/AddTodoForm.tsx'
            with open(AddTodoFormContent, 'r') as file:
                AddTodoFormContentContent = file.read()
                
            TodoContent = 'frontend/src/pages/Todo.tsx'
            with open(TodoContent, 'r') as file:
                TodoContent = file.read()
                
                
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                # You can change this to another model like gpt-3.5-turbo or gpt-4
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
                                    f"```Create a React CRUD application for the `{module}` module"
                                    f"For this data json : ```{json_structure}```"
                                    f"Use these methods of {module.capitalize()}Service\n"
                                    f"{services_list(module)}\n"
                                    "Here is example file for your reference for `todo` module\n"
                                    f"frontend/src/pages/Todo.tsx```{TodoContent}```\n"
                                    f"frontend/src/components/TodoItem.tsx```{TodoItemContent}```\n"
                                    f"frontend/src/components/AddTodoForm.tsx```{AddTodoFormContentContent}```\n"
                                    
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
            print(f"Error fetching response: {str(e)}")
            return f"Error fetching response: {str(e)}"

    def get_ai_response2(self, json_item):
        module = json_item["module"]
        """Function to get a response from the AI."""
        try:
            app_file_path = 'frontend/src/App.tsx'
            with open(app_file_path, 'r') as file:
                app_file_content = file.read()
            
            home_file_path = 'frontend/src/components/HomePage.tsx'
            with open(home_file_path, 'r') as file:
                home_file_content = file.read()
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                # You can change this to another model like gpt-3.5-turbo or gpt-4
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
                                "text": f"here is the `App.tsx` file  you've to add `{module}` rounter and add imports in this\n{app_file_path}```{app_file_content}```\n\n\nhere is the home page and you've to add {module} link in  this page\n{home_file_path}```{home_file_content}```"
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
        with open('engine/master.json', 'r') as file:
            json_data = json.loads(file.read())
            for json_item in json_data:
                # Get response from AI
                response = self.get_ai_response(json_item)
                result = self.write_response_to_file(response)
                response = self.get_ai_response2(json_item)
                result = self.write_response_to_file(response)
                print(json_item["module"], "done")

