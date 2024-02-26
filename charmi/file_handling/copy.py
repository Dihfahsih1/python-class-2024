import shutil 

source_file1 = 'files/data.txt'
source_file2 = 'files'

destination_file1 = 'files/data1.txt'

# shutil.copy(source_file1, destination_file1)       #this has already copied

destination_file2 = 'files/data2.txt'  
destination_file3 = 'files/data2/'
try:
    # shutil.copy(source_file1, destination_file2)    #this shows the time when the file was copied
    shutil.copytree(source_file2, destination_file3)    #this copies directories
except Exception as e:
    print(f"{e}")
