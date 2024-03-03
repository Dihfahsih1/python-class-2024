import zipfile

with zipfile.Zipfile("functions/sample_zip.zip","w") as zip_file:
    zip_file.write = ("assignments/data.txt")