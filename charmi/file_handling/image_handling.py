#we have binary mode  "rb", "wb", "ab"

with open("image1.png", "rb") as data:
    binary_data = data.read()
    print(binary_data)
