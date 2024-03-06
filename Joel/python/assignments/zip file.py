import zipfile


# Extract all contents of a zip file
with zipfile.ZipFile('example.zip', 'r') as zip file
    zip_ref.extractall('extracted_folder')