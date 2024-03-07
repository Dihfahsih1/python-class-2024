from zipfile import ZipFile

with ZipFile('New_zip.zip' , 'r') as my_zip:
    #to list names of things in the zip file
    print(my_zip.namelist())

    #to extract
    #my_zip.extractall('name_for_directory')

    # to extract single file
    #my_zip.extract('name_of_file_to_extract')
