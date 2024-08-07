import os
import pathlib

# Define the directories and their associated file extensions
DIRECTORIES = {
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".svg", ".heif", ".psd"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg", ".mpeg"],
    "MUSIC": [".aac", ".aa", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", ".msv", ".ogg", ".oga", ".raw", ".vox", ".wav", ".wma"],
    "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods", ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", ".pptx", ".csv"],
    "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar", ".xar", ".zip",".tgz"],
    "APPS": [".apk", ".bat", ".bin", ".cgi", ".pl", ".com", ".exe", ".gadget", ".jar", ".msi", ".py", ".wsf"],
    "WEB": [".asp", ".aspx", ".cer", ".cfm", ".cgi", ".pl", ".css", ".htm", ".html", ".js", ".jsp", ".part", ".php", ".rss", ".xhtml"],
    "PLAINTEXT": [".txt", ".in", ".out"],
    "PDF": [".pdf"]
    }

# Create a dictionary that maps file extensions to directory names
FILE_FORMATS = {file_format: directory
                for directory, file_formats in DIRECTORIES.items()
                for file_format in file_formats}

def organize_junk(target_folder):
    for item in os.scandir(target_folder):
        if item.is_dir():
            continue
        file_path = pathlib.Path(item)
        file_format = file_path.suffix.lower()

        # Check if the file is in the list of formats
        if file_format in FILE_FORMATS:
            directory_path = pathlib.Path(target_folder) / FILE_FORMATS[file_format]
            directory_path.mkdir(exist_ok=True)
            new_path = directory_path / file_path.name
            # Move the file to the new directory
            file_path.rename(new_path)
    
if __name__ == "__main__":
    target_folder = input("Enter the folder path: ")
    organize_junk(target_folder)
    print("Junk has been organized successfully!")
