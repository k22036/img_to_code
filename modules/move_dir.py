import shutil
import os
from natsort import natsorted as nat


def move_img_to_dir(target_dir, dest_dir):

    if not os.path.exists(target_dir):
        return False

    if not os.path.exists(dest_dir):
        return False

    try:
        target = os.listdir(target_dir)
        modified_target = [name.replace(".", "_") for name in target]

        for dest in os.listdir(dest_dir):
            modified_dest = dest.replace(".", "_")
            indices = [i for i, s in enumerate(
                modified_target) if modified_dest in s]

            dest_path = os.path.join(dest_dir, dest)

            for index in indices:
                # print(f"{modified_dest} : {modified_target[element]}")
                target_path = os.path.join(target_dir, target[index])
                shutil.move(target_path, dest_path)

        return True

    except Exception as e:
        print(f"{e}")
        return False
