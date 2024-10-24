from PIL import Image
from natsort import natsorted as nat
import pytesseract
import os


def det_name(image_dir, target_dir):
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')

    if not os.path.exists(image_dir):
        return False

    if not os.path.exists(target_dir):
        return False

    try:
        target = nat(os.listdir(target_dir))

        for i, filename in enumerate(nat(os.listdir(image_dir))):
            if filename.lower().endswith(image_extensions):

                image_path = os.path.join(image_dir, filename)
                target_path = os.path.join(target_dir, target[i])
                img = Image.open(image_path)
                text = pytesseract.image_to_string(img, lang='eng')

                new_name = f"{target_dir}{text}_{i+1}.png"

                os.rename(target_path, new_name.replace("\n", ""))

        return True
    except Exception as e:
        print(f"{e}")
        return False


def make_dir(image_dir, target_dir):
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')

    if not os.path.exists(image_dir):
        return False

    if not os.path.exists(target_dir):
        return False

    try:
        for filename in nat(os.listdir(image_dir)):
            if filename.lower().endswith(image_extensions):

                # 画像からファイル名を取得
                image_path = os.path.join(image_dir, filename)
                img = Image.open(image_path)
                text = pytesseract.image_to_string(img, lang='eng')

                target_path = os.path.join(
                    target_dir, (text.replace(".", "_")).replace("\n", ""))
                if not os.path.exists(target_path):
                    os.mkdir(target_path)

        return True
    except Exception as e:
        print(f"{e}")
        return False
