from zipfile import ZipFile


with ZipFile('python_class.zip', 'w') as zipf:
    zipf.write('file1.txt')
    zipf.write('file2.txt')