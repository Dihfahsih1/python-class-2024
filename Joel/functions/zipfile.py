from zipfile import zipFile


with zipfile.ZipFile('python_class.zip', 'w') as zipf:
    zipf.write('file1.txt')
    zipf.write('file2.txt')