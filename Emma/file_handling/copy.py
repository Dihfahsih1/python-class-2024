import shutil


source = "files/data.txt"
destination = "files/new_data.txt"
shutil.copy(source,destination)

try:
    shutil.copystat(source,destination)

except Exception as e:
    print(f"{e}")





#shutil.copytree() copys the folder
#shutil.copy() copys the file
#shutil.copystat() copys the 