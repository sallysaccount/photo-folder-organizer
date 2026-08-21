from PIL import Image
from PIL.ExifTags import TAGS, IFD
import re, os

# Will try to get Metadata from EXIF DateTimeOriginal, will fall back EXIF DateTime
def get_exif(file_path):

    with Image.open(file_path) as image:            # Open the image
        exif_data = image.getexif()                 # Extract the exif metadata
        exif_ifd = exif_data.get_ifd(IFD.Exif)      # Opening nested "EXIF IFD" where DateTimeOriginal is

        for tag_id, value in exif_ifd.items():      # Loop through all tags in current exifdata
            tag_name = TAGS.get(tag_id, tag_id)     # Getting the tag name instead of tag id

            if tag_name == "DateTimeOriginal":
                return value

        # DateTimeOriginal tag was not found, will check DateTime tag
        for tag_id, value in exif_data.items():     # Loop through all tags in current exifdata
            tag_name = TAGS.get(tag_id, tag_id)     # Getting the tag name instead of tag id

            if tag_name == "DateTime":
                return value

    return None     # Line executed if loop finished without finding tag

# Will try to read screenshot filename when unable to find EXIF
def get_date_from_filename(file_path):
    filename = os.path.basename(file_path)          # Using OS to extract final filename from the file path

    pattern = r"(\d{4})-(\d{2})-(\d{2})"            # Looking for date pattern (YYYY-MM-DD)
    match = re.search(pattern, filename)            # Using RE to match pattern, not just the start, anywhere inside the filename
    if match:
        year = match.group(1)                       # group(1) is first match (\d{4})
        month = match.group(2)                      # group(2) is second match (\d{2})
        return year, month

    return None                                     # If unable to find pattern, return none

# Returning timestamp YYYY, MM from EXIF or filename and if unable to find return unknown
def photo_date(file_path):

    date = get_exif(file_path)                      # Look for timestamp using get_exif
    if date is not None:                            # If date is found ... convert EXIF string into simple Year and Month
        year = date[0:4]
        month = date[5:7]
        return year, month

    date = get_date_from_filename(file_path)        # Look for timestamp using get_date_from_filename
    if date is not None:                            # If date is found ... return (date already formatted correctly)
        return date

    return None                                     # Unable to find any timestamp

# testing the function
if __name__ == "__main__":
    test_path = r"C:\Users\sally\OneDrive\Pictures\Screenshots\Screenshot 2026-05-25 162745.png"   # Windows
    result = photo_date(test_path)
    print(f"Date found: {result}")