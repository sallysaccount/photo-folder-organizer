Photo Organizer Summary

Photo Organizer is a Python application that automatically organizes photos by month and year using EXIF metadata and filename based detection. Just drag and drop!
Videos and files with unknown dates are handled separately, sorted into their own folders. The original photos are never modified.

This was designed to help organize photos and can be used to conveniently transfer to an external hard drive or save to the cloud.

Installation

Option One: Download the Zip File (Recommended)
1. Go to https://github.com/sallysaccount/photo-folder-organizer/releases/latest (the latest release)
2. Download the .zip file listed under Assets
3. Right Click and Extract All
4. Open the extracted folder and double click PhotoOrganizer.exe (PhotoOrganizer Type: Application)
    - If Windows shows a "Protected PC warning" click more info, then click run anyway

Option Two: With GitHub
git clone https://github.com/sallysaccount/photo-folder-organizer.git
cd photo-folder-organizer
pip install -r requirements.txt
python main.py

Quick Start
1. Drag and Drop your photos to the designated window, or click browse to select the files
   - Browse is beneficial if your device does not allow drag and drop
2. Photo Organizer sorts and copies the files into 
   - Desktop / Photo Organizer / <year> / <month> for photos with detected dates
   - Desktop / Photo Organizer / Videos for videos
   - Desktop / Photo Organizer / Unknown Date for photos with no detected dates
3. Once the photos are processed, a summary screen will show the number of processed photos, how many skipped due to errors, and the route to view your folders 

* Note: All files are copied, never moved. The originals are untouched

Output

How it Works
- The user drags and drops photos and/or videos into the application, or selects them using browse
- The program determines each files date using EXIF metadata
  - If EXIF data is unavailable, the filename is checked to determine a date. If no detected date, the photos will be placed in the Unknown Date folder
- Files are categorized by their type, photo or video and detected date
- Photos are copied into folders by <year> then <month>
- Videos are copied into a folder labeled Videos
- Photos without a detected date are copied into a folder labeled Unknown Date
- Duplicates and unreadable files are skipped and reported in the summary screen

Features
- Drag and Drop or Browse Button
- Date detection using EXIF metadata and filename date parsing
- Videos routed to their own folder (not organized by date)
- Error Handling to detect duplicated and skip unreadable or invalid files
- Responsive UI allowing file processing to run separately from the main UI thread

Built With
- Python
- Tkinter and tkinterdnd2 for drag and drop GUI
- sv-ttk for styling
- Pillow for EXIF metadata reading
- Python Libraries including pathlib, shutil, and threading

Future Improvements
- Video Metadata support
  - Videos are stored in an unsorted file due to having a different metadata then photos, would like to update this feature
- Additional Styling
  - Would like to improve and modernize the UI

Notes
This is a solo project, used for educational purposes. 
I was able to successfully use the program, sorting over 10,000 photos and videos. Then taking those sorted folders and dropping them into an external hard drive. 
