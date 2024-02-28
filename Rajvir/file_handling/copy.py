import shutil

source_file = "files/data.txt"

replace_file = "files/data1.txt"

try:
    shutil.copy(source_file, replace_file)

except Exception as e:
    print(f"{e}")

# copying directory...
source_file = "files"

replace_file = "files/data2/"

try:
    shutil.copytree(source_file, replace_file)

except Exception as e:
    print(f"{e}")


