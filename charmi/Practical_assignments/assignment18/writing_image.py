from PIL import Image

def image_handling():

    image = Image.open('img.jpg')

    rotated_image = image.rotate(200)
    print(rotated_image)

image_handling()