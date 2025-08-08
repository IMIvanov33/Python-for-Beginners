from pathlib import Path  # Import the Path class from the pathlib module

# Create a Path object pointing to the current directory ("" is treated as ".")
path = Path("")

# Loop through all files in the current directory that end with ".py"
for file in path.glob("*.py"):
    # Print the name of each .py file found
    print(file)
