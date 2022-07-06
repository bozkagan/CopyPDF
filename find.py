import os
import shutil

#Filling paths.
dst_path = r"" #Destination path
src_path = r"" #Source path

res = []

# os.walk() returns subdirectories, file from current directory and 
# And follow next directory from subdirectory list recursively until last directory
for root, dirs, files in os.walk(src_path):
    for file in files:
        if file.endswith(".pdf"):
            res.append(os.path.join(root, file))

for f in res:
    shutil.copy(f,dst_path)
    print(f)
