import os
import subprocess

# Set the correct path to the directory containing the STL files
path = os.path.join(os.getcwd(), "22_6sides_passage")

os.chdir(path)
files = os.listdir(path)
files.sort()

num = len(files)
print(files)
i = 0
for file in files:
    if os.path.isfile(os.path.join(path, file)):
        print(i, end=' ')
        i += 1
        print(file)
        res = subprocess.run(['binvox', '-d', '64', file], capture_output=True)
        os.remove(os.path.join(path,file))
