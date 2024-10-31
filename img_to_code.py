import os
from dotenv import load_dotenv
import google.generativeai as genai
import PIL.Image
import time

# .envファイルの読み込み
load_dotenv()

# API-KEYの設定
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

gemini_flash = genai.GenerativeModel(model_name="gemini-1.5-flash")

img_dir_path = "img/split_dir"
dirs_in_img = os.listdir(img_dir_path)
dirs_in_img = [dir for dir in dirs_in_img if os.path.isdir(
    f"{img_dir_path}/{dir}")]
output_files = os.listdir("output")

# img_files = []
img_files = dict()
for dir in dirs_in_img:
    # img_files += [f"{dir}/{file}" for file in os.listdir(
    #     f"{img_dir_path}/{dir}")]
    img_files[dir] = [f"{dir}/{file}" for file in os.listdir(
        f"{img_dir_path}/{dir}")]

for img_dir in img_files:
    time.sleep(2)
    while True:
        try:
            # output_name = ".".join(img_file.split('/')[-1].split(".")[:-1])
            output_name = ".".join(
                img_files[img_dir][0].split('/')[-1].split(".")[:-1])

            # if ".DS_Store" in img_file or output_name in output_files:
            #     break

            # img = PIL.Image.open(f"{img_dir_path}/{img_file}")
            imgs = [PIL.Image.open(f"{img_dir_path}/{img_file}")
                    for img_file in sorted(img_files[img_dir]) if
                    ".DS_Store" not in img_file and img_file.split('/')[-1] not in output_files]
            prompt = [
                """
                Please accurately transcribe the program code contained in the following image and present it in the specified format:
                - Use a code block for the output.
                - Ensure the transcribed code exactly matches the code in the image, including all syntax, indentation, and formatting.
                """,
                *imgs
            ]
            response = gemini_flash.generate_content(prompt)

            # 出力のコードの部分だけをファイルに出力
            text = response.text.split("```")[1].split("\n")[1:]
            with open(f"output/{output_name}", "w") as file:
                file.write("\n".join(text))

        except Exception as e:
            print(f"Error: {dir}")
            print(f"Error: {e}")
            if "429" in str(e) or "finish_message" in str(e):
                time.sleep(30)
                continue
            elif ".DS_Store" in str(e):
                break
        break
