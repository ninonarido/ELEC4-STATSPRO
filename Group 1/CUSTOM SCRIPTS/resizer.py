from PIL import Image, ExifTags
import os

# Specify the directory where your images are located
input_directory = 'ORGANIZED_DATASETS/Food and Groceries/1667 - NON PERSONAL INFO/1667'
# Specify the directory where you want to save the resized images
output_directory = 'ORGANIZED_DATASETS/Food and Groceries/1667 - NON PERSONAL INFO/1667'
# Define the target size (768, 1024 pixels)
target_size = (768, 1024)

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# List all files in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
        # Open the image file
        with Image.open(os.path.join(input_directory, filename)) as img:
            # Check if the image has Exif data
            if img._getexif():
                # Extract the Exif orientation tag
                for tag, value in img._getexif().items():
                    if tag in ExifTags.TAGS and ExifTags.TAGS[tag] == 'Orientation':
                        orientation = value
                        break
                else:
                    orientation = 1
            else:
                orientation = 1

            # Apply orientation
            if orientation in (2, 4, 5, 7):
                img = img.transpose(Image.FLIP_LEFT_RIGHT)
            if orientation in (3, 4, 6, 7):
                img = img.transpose(Image.ROTATE_180)
            if orientation in (5, 6):
                img = img.transpose(Image.FLIP_TOP_BOTTOM)

            # Resize the image to the new target size while preserving its aspect ratio
            img.thumbnail(target_size)

            # Create a new blank image with the new target size
            new_img = Image.new("RGB", target_size)

            # Paste the resized image onto the blank image to ensure it's centered
            new_img.paste(img, ((target_size[0] - img.width) // 2, (target_size[1] - img.height) // 2))

            # Save the final image with a new name in the output directory
            new_filename = os.path.splitext(filename)[0] + '.png'
            new_img.save(os.path.join(output_directory, new_filename), "PNG")

print("Images have been resized and reoriented.")