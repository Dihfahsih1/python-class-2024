import shutil

source_file="files"

destination_file="files/data2/"
try:
    shutil.copytree(source_file, destination_file)
except Exception as e:
    print(f"{e}")
    