from zipfile import ZipFile

zip_file = 'assignment_files/sample_zipfile.zip'

try:
    with ZipFile(zip_file, 'r') as zip:
        zip.printdir()

except Exception as e:
    print(f"{e}")
