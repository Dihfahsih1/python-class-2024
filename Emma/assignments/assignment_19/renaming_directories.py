import os


def renaming_directories():
    src = 'assignment_19/files/text.txt'
    dst = 'assignment_19/files/data_text.txt'

    os.rename(src,dst)


renaming_directories()
   
