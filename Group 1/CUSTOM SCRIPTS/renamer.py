import os

def rename_images(input_directory, output_directory, identifier):
    if not os.path.exists(input_directory):
        print(f"Input directory '{input_directory}' does not exist.")
        return

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    file_list = os.listdir(input_directory)
    count = 1

    for filename in file_list:
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
            # Get the file extension
            file_extension = os.path.splitext(filename)[1]

            # Create the new filename with the identifier and incrementing number (clfa_1.png, clfa_2.png)
            new_filename = f"{identifier}_{count}{file_extension}"

            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, new_filename)

            # Rename the file and move it to the output directory
            os.rename(input_path, output_path)
            count += 1

    print("Image files renamed and saved to the output directory.")

if __name__ == "__main__":
    #Paste your input and output directories here
    input_directory = "ORGANIZED_DATASETS/Food and Groceries/1667 - NON PERSONAL INFO/1667" 
    output_directory = "ORGANIZED_DATASETS/Food and Groceries/1667 - NON PERSONAL INFO/1667" 

    #Paste your identifier here (clfa, elec, skca, hoap, fogr, hone)
    identifier = "fogr_non"

    rename_images(input_directory, output_directory, identifier)