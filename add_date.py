import os
from datetime import datetime

# Get today's date in YYYY-MM-DD format
today = datetime.now().strftime('%Y-%m-%d')
folder_path = 'Test_data'

def add_date_to_filenames(directory):
    # Check if directory exists
    if not os.path.exists(directory):
        print(f"Directory '{directory}' not found.")
        return

    # Iterate through files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Ensure it's a file, not a directory
        if os.path.isfile(file_path):
            # Create the new filename with the date prefix
            new_filename = f"{today}_{filename}"
            new_file_path = os.path.join(directory, new_filename)
            
            # Rename the file
            os.rename(file_path, new_file_path)
            print(f"Renamed: {filename} -> {new_filename}")

if __name__ == "__main__":
    add_date_to_filenames(folder_path)
