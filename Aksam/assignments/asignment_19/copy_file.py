
def copy_file(source_file, new_file):
    try:
        with open(source_file, "rb") as src_file:
            with open(new_file, "wb") as dest_file:
                dest_file.write(src_file.read())
        print(f"File {source_file} copied to {new_file} successfuly")
    except IOError as e:
        print(f"Error: {e}")


source_file = input("Enter the file to copy from: ")
new_file = input("Enter the file to copy to: ")     
copy_file(source_file, new_file)