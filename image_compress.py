# %%
import os
from PIL import Image
import argparse

def replace_path(file_path_png, file_path_jpg, directory, full_check=True):
    """Replace the file path of the original .png to the new .jpg file inside all the .md files. If no "directory" is defined, it will replace at the current folder level.

    Args:
        file_path_png (str): Full path to the .png file.
        file_path_jpg (str): Full path to the new .jpg file.
        directory (str): Path to the Vault.
        full_check (bool, optional): To check from the Vault's base directory
    """
    if not full_check:
        directory = os.path.dirname(os.path.dirname(file_path_jpg))
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='UTF-8') as f:
                    content = f.read()

                    file_path_png = os.path.basename(file_path_png)
                    file_path_jpg = os.path.basename(file_path_jpg)

                    if file_path_png in content:
                        content = content.replace(file_path_png, file_path_jpg)
                        with open(file_path, 'w', encoding='UTF-8') as f:
                            f.write(content)

def png_to_jpg(file_path_png, quality):
    """Compress the .png files to .jpg.

    Args:
        file_path_png (str): Full path to the .png file.
        quality (int, optional): Compress value. Higher the number, the best the quality and bigger the file size. Defaults to 80.

    Returns:
        (str, str): Path to the original .png file, and path to the new .jpg file.
    """
    with Image.open(file_path_png) as png_image:
        file_path_jpg = os.path.splitext(file_path_png)[0] + ".jpg"
        png_image.convert('RGB').save(file_path_jpg, quality=quality)
    os.remove(file_path_png)
    return file_path_png, file_path_jpg

def run_directories_recursive(directory, full_check, quality):
    """Run the process recursively inside the directory, and if defined, the directory base. Also takes into account the quality

    Args:
        directory (str): Path to the Vault.
        full_check (bool): To check from the Vault's base directory
        quality (int): Compress quality
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.png') or file.endswith('.gif'):
                file_path = os.path.join(root, file)
                print(file_path)
                file_path_png, file_path_jpg = png_to_jpg(file_path, quality)
                replace_path(file_path_png, file_path_jpg, directory, full_check)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Find all .png files, convert them to .jpg and relink the .md')
    parser.add_argument('directory', type=str, help='Path to the Vault.')
    parser.add_argument('-f', '--full_check', type=bool, required=False, default=True, help='Check from the base directory of the Vault.')
    parser.add_argument('-q', '--quality', type=int, required=False, default=80, help='Path to the Vault. If not defined, the script will only replace on .md at one level up to the .png.')

    # Parse the arguments
    args = parser.parse_args()

    run_directories_recursive(args.directory, args.full_check, args.quality)

# %%
# Tested on Windows
# Referenced at
# https://gist.github.com/juanbretti/7f3dfc98b39e3d4216c275232a56305c
# https://forum.obsidian.md/t/find-all-png-files-convert-them-to-jpg-rename-to-png/50478/6
#
# Ways to run the script
# python.exe "image_compress.py" "C:\Vault"
