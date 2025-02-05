import zipfile
import os

# Define the path to the zip file and the extraction directory
zip_file_path = 'downloads/FirstProject.zip'
extraction_dir = 'downloads/FirstProject'

# Create the extraction directory if it doesn't exist
if not os.path.exists(extraction_dir):
    os.makedirs(extraction_dir)

# Unzip the file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extraction_dir)

print(f'Unzipped {zip_file_path} to {extraction_dir}')
import shutil

# Define the source and destination directories
source_pages_dir = 'downloads/FirstProject/src/pages'
dest_pages_dir = 'frontend/src/pages'
source_components_dir = 'downloads/FirstProject/src/components'
dest_components_dir = 'frontend/src/components'
source_public_dir = 'downloads/FirstProject/public'
dest_public_dir = 'frontend/public'

# Create the destination directories if they don't exist
os.makedirs(dest_pages_dir, exist_ok=True)
os.makedirs(dest_components_dir, exist_ok=True)
os.makedirs(dest_public_dir, exist_ok=True)

# Copy the content from source to destination directories
shutil.copytree(source_pages_dir, dest_pages_dir, dirs_exist_ok=True)
shutil.copytree(source_components_dir, dest_components_dir, dirs_exist_ok=True)
shutil.copytree(source_public_dir, dest_public_dir, dirs_exist_ok=True)

print(f'Copied content from {source_pages_dir} to {dest_pages_dir}')
print(f'Copied content from {source_components_dir} to {dest_components_dir}')
print(f'Copied content from {source_public_dir} to {dest_public_dir}')

# Python code to replace the word "HomePage" with "DesktopLaptop" in the file frontend/src/App.tsx

# Define the file path
file_path = 'frontend/src/App.tsx'

# Read the content of the file
with open(file_path, 'r') as file:
    content = file.read()

# Replace "HomePage" with "DesktopLaptop"
updated_content = content.replace('HomePage', 'DesktopLaptop')

# Write the updated content back to the file
with open(file_path, 'w') as file:
    file.write(updated_content)

print(f'Replaced "HomePage" with "DesktopLaptop" in {file_path}')

