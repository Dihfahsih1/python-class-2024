def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r')
            with open(destination_file, 'w') as destination:
                destination.write(sound.read())
        print(f"Content copied from '{source_file}'to '{destination_file}' successfully.")
    except FileNotFoundError:
        print(f"One of the files '{source_file}' or '{destination_file}' not found.")