import csv
import os
import requests
from PIL import Image
from io import BytesIO

# Function to download an image from a given URL
def download_image(image_url, download_dir, index, failed_urls):
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            # Convert .webp to .png
            with Image.open(BytesIO(response.content)) as img:
                filename = os.path.join(download_dir, f"{index}.png")
                img.save(filename, "PNG")

            print(f"Downloaded and converted: {filename}")
        else:
            print(f"Failed to download: {image_url}")
            # Store the failed URL in the list
            failed_urls.append(image_url)
    except Exception as e:
        print(f"Error: {e}")

# Function to download images from a CSV file
def download_images_from_csv(csv_file, download_dir):
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        index = 0  # Initialize an index variable
        failed_urls = []  # List to store failed URLs
        for row in csv_reader:
            image_url = row[0]  # Assuming the URLs are in the first column
            download_image(image_url, download_dir, index, failed_urls)
            index += 1  # Increment the index

        return failed_urls

if __name__ == "__main__":
    # Download images from CSV files
    csv_files = [
        "EXTRA DATASETS\EXTRA_CLOTHES.csv"
    ]

    base_download_dir = "EXTRA DATASETS"

    for csv_file in csv_files:
        category = csv_file.split('.')[0]  # Extract the category name from the CSV filename
        download_dir = os.path.join(base_download_dir, category)

        if not os.path.exists(download_dir):
            os.makedirs(download_dir)

        failed_urls = download_images_from_csv(csv_file, download_dir)
        print("Failed to download the following URLs:")
        for url in failed_urls:
            print(url)
