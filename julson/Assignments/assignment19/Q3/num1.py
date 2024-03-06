import zipfile

with zipfile.ZipFile('data2.zip', 'w') as zipf:
    zipf.write('data.txt')
    zipf.write('data2.txt')