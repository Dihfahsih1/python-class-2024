#this is reading and appending an image file..
#writing.# image is in binary, so it will be read like that :>

with open('img.jpg', "rb") as imagefile:
    img_binary_data =imagefile.read()
    print(img_binary_data)

with open("new_img.jpg","ab") as imagefile:
    appended_binary_img =  imagefile.write(img_binary_data)
    print(appended_binary_img)