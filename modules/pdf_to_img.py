from pdf2image import convert_from_path
import os


def pdf_to_images(pdf_path, output_dir, file_name):

    if not pdf_path.lower().endswith('.pdf'):
        return False

    if not os.path.exists(pdf_path):
        return False

    if not os.path.exists(output_dir):
        return False

    try:
        images = convert_from_path(pdf_path)
        for i, image in enumerate(images):

            image.save(f'{output_dir}{file_name}_{i+1}.png', 'PNG')

        return True
    except Exception as e:
        print(f"{e}")
        return False
