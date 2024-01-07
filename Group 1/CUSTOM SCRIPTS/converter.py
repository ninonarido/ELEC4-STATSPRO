from PIL import Image
import os

# Specify the directory where your image files are located
input_directory = 'ORGANIZED_DATASETS/Food and Groceries/417 - FACE'

# List all files in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith(('.webp', '.jpg', '.jpeg', '.png')):
        # Open the image file
        with Image.open(os.path.join(input_directory, filename)) as img:
            # Remove the file extension and add .png to the filename
            new_filename = os.path.splitext(filename)[0] + '.png'

            # Save the image as .png in the input directory, overwriting the original file
            img.save(os.path.join(input_directory, new_filename), "PNG")

print("Images have been converted to .png and original files have been overwritten.")
