#we have binary mode  "rb", "wb", "ab"

with open("files/image.png", "rb") as data:
    binary_data = data.read()
    print(binary_data)