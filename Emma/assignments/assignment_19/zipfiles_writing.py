from zipfile import ZipFile

with ZipFile('New_zip.zip','w') as new_zip:
    new_zip.write('text1.txt')
    new_zip.write('text2.txt')
    print("done")


#to compress 
    
#with ZipFile('New_zip.zip','w',compression=zipfile.ZIP_DEFLATED) as new_zip:
    #new_zip.write('text1.txt')
    #print("done")

# extracting

    