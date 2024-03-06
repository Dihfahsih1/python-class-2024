from PTL import Image

def append_images_horizontally(image1_path, image2_path, output_path):
    # Open images
    image1 = Image.open('image1.jpg')
    image2 = Image.open('image2.jpg')

    # Calculate the width and height of the combined image
    width = image1.width + image2.width
    height = max(image1.height, image2.height)

    # Create a new image with the combined width and height
    new_image = Image.new('RGB', (width, height))

    # Paste the first image at the left side of the new image
    new_image.paste(image1, (O,O))

    # Paste the second image at the right side of the new image
    new_image.paste(image2,(image1.width, O))

    # Save or display the new image
    new_image.save('combined_image.jpg')
    new_image.show()