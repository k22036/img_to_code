from modules import pdf_to_img as convert
from modules import img_crop as crop
from modules import det_name as detection
from modules import move_dir as move


filename = "RSS.pdf"


def main():
    pdf_path = "input_pdf/" + filename
    output_dir = "img/temp/"
    file_name = "raw_img"

    print("call: pdf_to_images")
    res = convert.pdf_to_images(pdf_path, output_dir, file_name)
    print('succes' if res else 'failed')

    image_dir = 'img/temp/'
    output_dir = 'img/code_img/'
    file_name = "code_img"
    crop_area = (118, 0, 1600, 2195)

    print("call: crop")
    res = crop.crop(image_dir, output_dir, file_name, crop_area)
    print('succes' if res else 'failed')

    image_dir = 'img/temp/'
    output_dir = "img/name_img/"
    file_name = "name_img"
    crop_area = (0, 0, 850, 110)

    print("call: crop")
    res = crop.crop(image_dir, output_dir, file_name, crop_area)
    print('succes' if res else 'failed')

    input_dir = "img/name_img/"
    output_dir = "img/code_img/"

    print("call: det_name")
    # コード画像のファイル名変更
    res = detection.det_name(input_dir, output_dir)
    print('succes' if res else 'failed')

    input_dir = "img/name_img/"
    output_dir = "img/split_dir/"
    print("call: make_dir")
    res = detection.make_dir(input_dir, output_dir)
    print('succes' if res else 'failed')

    target_dir = "img/code_img/"
    destination_dir = "img/split_dir/"
    print("call: move_img_to_dir")
    move.move_img_to_dir(target_dir, destination_dir)
    print('succes' if res else 'failed')


if __name__ == "__main__":
    main()
