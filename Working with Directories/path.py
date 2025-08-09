# Absolute path example: C:\Program Files\alabala  (this is a full path from the root)
# The line below is a relative path example — it's based on the current folder.

# Import the Path class from the pathlib module for working with file paths
from pathlib import Path

# Create a Path object for a folder (or file) named "Packages" in the current directory
path = Path("Packages")

# Check if the path "Packages" exists and print True or False
print(path.exists())
