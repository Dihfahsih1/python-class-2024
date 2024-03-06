import zipfile
import os

directory = 'my_directory/'

with zipfile.ZipFile('output.zip', 'w') as zipf:
    for root, dirs, files in os.walk(directory):
        for file in files:
            zipf.write(os.path.join(root, file))