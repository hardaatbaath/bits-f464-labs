import os
import shutil

def move_mask_images(src_folder, dest_folder):
    # Create the destination folder if it doesn't exist
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # Iterate through all subfolders in the source folder
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            # Check if the file is an image and ends with _mask.tif
            if file.lower().endswith('_mask.tif'):
                src_file_path = os.path.join(root, file)
                dest_file_path = os.path.join(dest_folder, file)
                
                # Move the image file to the destination folder
                shutil.move(src_file_path, dest_file_path)
                print(f"Moved {src_file_path} to {dest_file_path}")

if __name__ == "__main__":
    # Specify the source folder
    src_folder = "./dataset/" 

    # Specify the destination folder
    dest_folder = "./masks"

    # Move the mask images
    move_mask_images(src_folder, dest_folder)
