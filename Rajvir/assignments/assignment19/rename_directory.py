#renaming a directory...

import os 

oldname= "directory1"
newname= "directory2"

try:
    os.rename(directory1,directory2)

except Exception as e:
    print(f"{e}")

