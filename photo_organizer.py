from pathlib import Path
from metadata import photo_date
from folder import get_labeled_folder, copy_photo

# Function to be called for each dropped file
def photo_organizer(source_file, base_path):
    photo_route = photo_date(source_file)                         # Getting photo date, returning Year and Month or None
    if photo_route is None:                                       # No date Found
        print("No photo date found, stored in folder Unknown Date")
        folder = Path(base_path, "Unknown Date")            # Unknown date folder path
        folder.mkdir(parents=True, exist_ok=True)                 # Create only if it doesn't exist
    else:                                                         # Date is Found
        year, month = photo_route                                 # Needing to split the Year and Month apart each in their own variable
        folder = get_labeled_folder(base_path, year, month)       # Creating or getting the correct Year and Month Labeled Folder

    copy_photo(source_file, folder)                               # Copy photo to destination

# testing the function
if __name__ == "__main__":
    test_source = Path(r"C:\Users\sally\OneDrive\Pictures\IMG_2297.jpg")
    test_base = r"C:\Users\sally\OneDrive\Pictures\Organized"
    photo_organizer(test_source, test_base)