import zipfile

files = ['file1.txt', 'file2.txt', 'file3.txt']

with zipfile.ZipFile('output.zip', 'w') as zipf:
    for file in files:
        zipf.write(file)