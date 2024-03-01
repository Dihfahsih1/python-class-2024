#renaming a directory...

import os 

oldname= "directory1"
newname= "directory2"

try:
    os.rename(oldname,newname)

except Exception as e:
    print(f"{e}")
