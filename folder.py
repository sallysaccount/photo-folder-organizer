from pathlib import Path
import shutil
import random
import calendar

# Creating a new folder
def get_labeled_folder(base_path, year, month):

    month = calendar.month_name[int(month)]                         # Convert 07 to July

    folder = Path(base_path, year, month)
    folder.mkdir(parents=True, exist_ok=True)                       # Creates folder (Create missing parent folder, won't throw error if folder already exists)
    return folder

# Creating a copy photo for filenames with same name but different information, specifically comparing the file sizes
def copy_photo(source_file, labeled_folder):
    destination_path = labeled_folder / source_file.name            # Where the file will go inside the labeled folder

    if destination_path.exists():                                   # Checking if a file already exists by comparing size (so we don't duplicate)
        file_size = source_file.stat().st_size
        destination_size = destination_path.stat().st_size

        if file_size == destination_size:                           # Do not duplicate, file sizes are the same
            print(f"Duplicate file, will not make copy")
            return False
        else:
            new_name = f"{source_file.stem}_{random.randint(1,99)}{source_file.suffix}"    # creating new filename so files are no longer duplicates
            new_destination_path  = labeled_folder / new_name       # Where the file will go inside the labeled folder
            shutil.copy2(source_file, new_destination_path)         # Copy to new path
            print(f"Copied file and renamed to {new_name}")
            return True

    shutil.copy2(source_file, destination_path)                     # Copy of original path
    return True

# testing the function
if __name__ == "__main__":
    destination = get_labeled_folder(r"C:\Users\sally\OneDrive\Pictures\Organized", "2024", "07")
    print(f"Folder: {destination}")

    source = Path(r"C:\Users\sally\OneDrive\Pictures\IMG_2297.jpg")
    copy_photo(source, destination)