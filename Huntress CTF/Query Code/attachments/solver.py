from pyzbar.pyzbar import decode
from PIL import Image

def read_qr_code(img_path):
    image = Image.open(img_path)

    qr_code = decode(image)

    code = qr_code[0]
    data = code.data.decode("utf-8")
    print(data)

img_path = "./query_code.png"
read_qr_code(img_path)