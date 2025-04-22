import os
import shutil

source_file = "data/source.txt"
target_dir = "backup"

# Create target subdirectory
os.makedirs(target_dir, exist_ok=True)

# Copy file
shutil.copy(source_file, os.path.join(target_dir, "copied.txt"))
print("File copied successfully!")
