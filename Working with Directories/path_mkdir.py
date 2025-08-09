from pathlib import Path  # Import the Path class from the pathlib module

# Create a Path object pointing to a folder named "Emails" in the current directory
path = Path("Emails")

# Create the folder "Emails"
print(path.mkdir())
