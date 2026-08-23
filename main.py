import threading
import sv_ttk
from tkinter import ttk
from pathlib import Path
from folder import copy_photo
from tkinter import messagebox, filedialog
from tkinterdnd2 import DND_FILES, TkinterDnD
from photo_organizer import photo_organizer

desktop_path = Path.home() / "Desktop" / "Photo Organizer"      # Path I choose to have folder automatically stored
print(f"Photo Organizer Desktop path: {desktop_path}")          # Prints path of the folder on console

video_extension = [".mp4", ".mov", ".avi", ".webm", ".mpg", ".flv", ".ogg", ".mts"]     # Pillow EXIF does not read videos, alternate route for Videos to a separate folder (not organized by year)

root = TkinterDnD.Tk()                                          # Using TkinterDnD supports Drag and Drop
root.title("Photo Organizer")                                   # Setting window name
root.geometry("400x400")                                        # Setting window width and height

sv_ttk.set_theme("dark")                                        # Found themes for styling through sv-ttk
header = ttk.Label(root, text="Photo Organizer", font=("Times New Roman", 20))
header.pack(pady=(20,0))

drop_zone = ttk.Label(root, text="Drag and Drop Photos Here", relief="ridge", anchor="center")      # Controls Boarder and Position of text for Drop
drop_zone.pack(fill="both", expand=True, padx=25, pady=25)                                          # Enlarging the Drop Zone
drop_zone.drop_target_register(DND_FILES)                                                           # GUI able to accept dropped files in drop_zone

def process_files(file_path):
    copied_count = 0                                                        # Tracks how many files are successfully counted
    skipped_count = 0                                                       # Tracks how many files hit an error and are skipped

    for path in file_path:
        try:                                                                # Error catching
            source_file = Path(path)                                        # Conver the string to a Path object (used when managing files and folders)
            file_extension = source_file.suffix.lower()                     # Getting the extension to use and compare

            if file_extension in video_extension:
                destination_folder = Path(desktop_path, "Videos")     # Path to have folder automatically for videos
                destination_folder.mkdir(parents=True, exist_ok=True)       # Creates folder (Create missing parent folder, won't throw error if folder already exists)
                copy_photo(source_file, destination_folder)
            else:
                photo_organizer(source_file, desktop_path)

            copied_count += 1                                               # Reached and count increases by one if no errors

        except Exception as error:
            print(f"Skipped {path} due to {error}")                         # If error, throw error message
            skipped_count += 1                                              # Reached and count increases by one if error

    # After the loop has completed, message summerizes to user
    messagebox.showinfo("Complete", f"Processed {copied_count} photos.\n" f"Skipped {skipped_count} photos due to errors.\n" f"Find your photo folders here: {desktop_path}")


def browse_files():
    file_path = filedialog.askopenfilenames(title="Select Photos")           # Opens window from OS to select photos from

    if file_path:
        print(f"Number of Files Dropped: {len(file_path)}")                 # Print message on consol with Drop is success

        thread = threading.Thread(target=process_files, args=(file_path,))  # Run and pass the data into the function and make them ordered in a list
        thread.start()                                                      # Start thread, running in background

browse_button = ttk.Button(root, text="Browse", command=browse_files)       # Browse button option to instead of drag and drop, route to browse instead
browse_button.pack(pady=10)                                                 # Styling to button

def on_drop(event):                                                         # Run when drop occurs, event contains details of what was dropped
    file_path = root.tk.splitlist(event.data)                               # Splits string into list of separate strings
    print(f"Number of Files Dropped: {len(file_path)}")                     # Print message on consol with Drop is success

    thread = threading.Thread(target=process_files, args=(file_path,))      # Run and pass the data into the function and make them ordered in a list
    thread.start()                                                          # Start thread, running in background

drop_zone.dnd_bind("<<Drop>>", on_drop)                                     # Register the widget from library to accept dropped item
root.mainloop()                                                             # Keep window open and running for user interaction