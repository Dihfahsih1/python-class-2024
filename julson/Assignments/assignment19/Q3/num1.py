import zipfile

with zipfile.ZipFile('output.zip', 'w') as zipf:
    zipf.write('file.txt')