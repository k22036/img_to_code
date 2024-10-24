import os
import shutil

dirs = ["img/name_img/", "img/temp/", "img/split_dir/"]


def remove_files(dirs):
    for dir in dirs:
        if os.path.exists(dir):
            files = os.listdir(dir)

            # ディレクトリ内のファイル，ディレクトリを削除
            for file in files:
                if os.path.isfile(dir + file):
                    os.remove(dir + file)
                elif os.path.isdir(dir + file):
                    shutil.rmtree(dir + file)


if __name__ == "__main__":
    remove_files(dirs)
    print("remove files")
