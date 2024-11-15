import os
import shutil

# Define the folder you want to organize
source_folder = '/path/to/your/folder'  # Update with the path to your folder

# Dictionary to map file extensions to folder names
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Audio': ['.mp3', '.wav'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Archives': ['.zip', '.tar', '.gz', '.rar']
}

# Create folders if they don't exist
def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Function to move files to respective folders
def organize_files():
    # Loop through all files in the folder
    for file_name in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file_name)

        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue

        # Get the file extension
        file_ext = os.path.splitext(file_name)[1].lower()

        # Move the file to the corresponding folder based on its extension
        moved = False
        for folder_name, extensions in file_types.items():
            if file_ext in extensions:
                folder_path = os.path.join(source_folder, folder_name)
                create_folder(folder_path)
                shutil.move(file_path, os.path.join(folder_path, file_name))
                print(f"Moved {file_name} to {folder_name} folder.")
                moved = True
                break

        # If the file extension doesn't match any predefined types, move it to 'Others'
        if not moved:
            other_folder = os.path.join(source_folder, 'Others')
            create_folder(other_folder)
            shutil.move(file_path, os.path.join(other_folder, file_name))
            print(f"Moved {file_name} to Others folder.")

if __name__ == "__main__":
    organize_files()
