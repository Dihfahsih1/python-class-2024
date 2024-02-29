import zipfile
# 1 extracting
with zipfile.ZipFile("template.zip", "r") as zip_ref:
    zip_ref.extractall("Extracted_data")
    

# 2 creating
with zipfile.ZipFile("new_Zip.zip", "w") as zip_ref:
    zip_ref.write("file2.txt")
    zip_ref.write("file2.txt")
    
    
# 3 Adding files to a zip file
with zipfile.ZipFile("template.zip", "a") as zip_ref:
    zip_ref.write("file.txt")