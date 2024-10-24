import os
from windowpackage import process_image, rename_files

def main():
    # Set the directory containing your files
    directory = 'Test_images/Slight under focus'

    # First, rename the files
    rename_files(directory)

    # Then process each image
    background_path = os.path.join(directory, 'background.tiff')
    for filename in os.listdir(directory):
        if filename.endswith('.tiff') and filename != 'background.tiff':
            image_path = os.path.join(directory, filename)
            print(f"Processing {image_path}")
            process_image(image_path, background_path)

if __name__ == "__main__":
    main()