import os

def create_folder(folder_path):
    """ Create a folder if it doesn't exist."""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def get_updated_file_path(updated_folder_path, file_name):
    """Generate the path for the updated file."""
    return os.path.join(updated_folder_path, "updated_" + file_name)