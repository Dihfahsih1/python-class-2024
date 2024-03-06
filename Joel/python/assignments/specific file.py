import zipfile


# Extract a specific file from a zip file
with zipfile.ZipFile('example.zip', 'r') as zip_ref:
    zip_ref.extract('file_inside_zip.txt', 'extracted_file.txt')