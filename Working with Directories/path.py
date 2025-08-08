# Absolute path -- C:\Program Files\alabala
# This here is a relative path.
from pathlib import Path

path = Path("Packages1")
print(path.exists())
