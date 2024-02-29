import shutil

source file="files/data10.txt"

destination file="files/data1"
try:
     shutil.copytree(source_file, destination_file)
except Exception as e:
    print(f"{e}")