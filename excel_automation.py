import os
from file_handler import create_folder, get_updated_file_path
from excel_processor import process_workbook

# Set directory paths
folder_path = "Transactions data"
updated_folder_path = "Updated Transactions"

# Create the updated folder
create_folder(updated_folder_path)

# Loop through all Excel files in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith(".xlsx"):
        file_path = os.path.join(folder_path, file_name)
        updated_file_path = get_updated_file_path(updated_folder_path, file_name)

        print(f"Processing file: {file_name}")
        process_workbook(file_path, updated_file_path)