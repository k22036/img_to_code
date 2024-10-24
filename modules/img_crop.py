from PIL import Image, ImageDraw
from natsort import natsorted as nat
import os

image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')


def crop(image_dir, output_dir, file_name, crop_area):

    if not os.path.exists(image_dir):
        return False

    if not os.path.exists(output_dir):
        return False

    try:
        for i, filename in enumerate(nat(os.listdir(image_dir))):
            if filename.lower().endswith(image_extensions):
                image_path = os.path.join(image_dir, filename)

                image = Image.open(image_path)

                cropped_image = image.crop(crop_area)

                output_path = f'{output_dir}{file_name}_{i+1}.png'
                cropped_image.save(output_path.replace("\n", ""), "PNG")

        return True
    except Exception as e:
        print(f"{e}")
        return False
