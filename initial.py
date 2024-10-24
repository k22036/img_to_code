import os


dirs = ["input_pdf", "output", "img", "img/code_img",
        "img/name_img", "img/temp", "img/split_dir/"]

for dir in dirs:
    if os.path.exists(dir):
        continue
    os.mkdir(dir)
