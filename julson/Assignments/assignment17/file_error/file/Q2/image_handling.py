from PIL import Image

# Create a new image with RGB color (red) and size 100x100 pixels
image = Image.new('RGB', (100, 100), color='red')

# Save the image to a file in binary mode
with open('red_image.png', 'wb') as file:
    image.save(file, format='PNG')