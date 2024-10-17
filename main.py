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

img_dir_path = "img"
img_files = os.listdir(img_dir_path)
output_files = os.listdir("output")

for img_file in img_files:
    time.sleep(3)
    while True:
        try:
            output_name = ".".join(img_file.split(".")[:-1])

            if ".DS_Store" in img_file or output_name in output_files:
                break

            img = PIL.Image.open(f"{img_dir_path}/{img_file}")
            prompt = [
                "次の画像に含まれるプログラムのコードを正確に文字起こしし、以下の形式で出力してください。\n・出力は必ずコードブロックを使い、画像のコードと完全に一致させること。", img]
            response = gemini_flash.generate_content(prompt)

            # 出力のコードの部分だけをファイルに出力
            text = response.text.split("```")[1].split("\n")[1:]
            with open(f"output/{output_name}", "w") as file:
                file.write("\n".join(text))

        except Exception as e:
            print(f"Error: {img_file}")
            print(f"Error: {e}")
            if "429" in str(e) or "finish_message" in str(e):
                time.sleep(30)
                continue
            elif ".DS_Store" in str(e):
                break
