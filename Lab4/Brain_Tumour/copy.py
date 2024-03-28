import os
import shutil

def copy_images(src_folder, dest_folder):
    # Create the destination folder if it doesn't exist
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # Iterate through all subfolders in the source folder
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            # Check if the file is an image
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.tif', '.bmp', '.tiff')):
                src_file_path = os.path.join(root, file)
                dest_file_path = os.path.join(dest_folder, file)
                
                # Copy the image file to the destination folder
                shutil.copy2(src_file_path, dest_file_path)
                print(f"Copied {src_file_path} to {dest_file_path}")

if __name__ == "__main__":
    # Specify the source folder
    src_folder = "./kaggle_3m/"

    # Specify the destination folder
    dest_folder = "./dataset/"

    # Copy the images
    copy_images(src_folder, dest_folder)
