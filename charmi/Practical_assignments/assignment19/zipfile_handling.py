import zipfile

#creating a zipfile

with zipfile.ZipFile("assignment_files/sample_zipfile.zip", "w") as zip_file:
    zip_file.write("assignment_files/data.txt")

#reading zip

with zipfile.ZipFile("assignment_files/sample_zipfile.zip", "r") as zip_file:
    zip_file.extract("assignment_files/data.txt")

#appending 

with zipfile.ZipFile("assignment_files/sample_zipfile.zip", "a") as zip_file:
    zip_file.write("assignment_files/data1.txt")


