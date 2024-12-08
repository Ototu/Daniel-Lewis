#AOA Project
#Date November 18,2024
#: Khadejah Benjamin-2208656 
# Ramon Johnston -2008317
#Daniel Lewis- 2202361 
# Rushane Green – 2006930 
# Chamarie Taylor – 2100037

import os
import time
from utilities import format_size
from sorting import merge_sort

class FileManagement:
    def __init__(self, current_path):
        self.current_path = current_path

    def list_directory(self, path, sort_key="name"):
        files_info = []
        try:
            files = os.listdir(path)
            sort_func = self.get_sort_key(sort_key)
            merge_sort(files, key_func=sort_func)

            for item in files:
                full_path = os.path.join(path, item)
                name, extension = os.path.splitext(item)
                extension = extension.lstrip('.') if extension else "Folder"
                
                size = format_size(os.stat(full_path).st_size) if os.path.isfile(full_path) else "-"
                modified_time = time.ctime(os.stat(full_path).st_mtime)
                files_info.append((name, extension, size, modified_time))
            return files_info
        except Exception as e:
            raise Exception(f"Failed to list directory: {e}")

    def get_sort_key(self, sort_key):
        if sort_key == "size":
            return lambda item: os.stat(os.path.join(self.current_path, item)).st_size if os.path.isfile(os.path.join(self.current_path, item)) else 0
        elif sort_key == "date":
            return lambda item: os.stat(os.path.join(self.current_path, item)).st_mtime
        return lambda item: item.lower()
