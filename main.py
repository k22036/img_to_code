import os
from dotenv import load_dotenv
import google.generativeai as genai
import PIL.Image

# .envファイルの読み込み
load_dotenv()

# API-KEYの設定
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

gemini_flash = genai.GenerativeModel(model_name="gemini-1.5-flash")

img_dir_path = "img"
img_files = os.listdir(img_dir_path)

for img_file in img_files:
    img = PIL.Image.open(f"{img_dir_path}/{img_file}")
    prompt = ["画像のコードを文字起こししてください．", img]
    response = gemini_flash.generate_content(prompt)

    output_name = ".".join(img_file.split(".")[:-1])
    # 出力のコードの部分だけをファイルに出力
    with open(f"output/{output_name}", "w") as file:
        file.write("\n".join(response.text.split("```")[1].split("\n")[1:]))
