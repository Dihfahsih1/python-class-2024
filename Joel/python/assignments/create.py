import zipfile

# Create a new zip file and add file to it
with zipfile.ZipFile('new_zip_file.zip', 'w') as zip_ref:
    zip_ref.writ('file1.txt!')
    zip_ref.write('file2.txt')