#AOA Project
#Date November 18,2024
#: Khadejah Benjamin-2208656 
# Ramon Johnston -2008317
#Daniel Lewis- 2202361 
# Rushane Green – 2006930 
# Chamarie Taylor – 2100037

from math import log  # Import log from math module

def format_size(size_bytes):
    """Convert bytes to a more readable format (e.g., KB, MB, GB)."""
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB")
    i = int(log(size_bytes, 1024))
    p = 1024 ** i
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"
