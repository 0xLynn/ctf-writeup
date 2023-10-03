# Query Code

> <p>What's this?</p>
> <p><a href="attachments/query_code.png">query_code</a></p>

## Path to Flag

Here's a simple script to read the `QR Code` content:

```
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
```

`flag{3434cf5dc6a865657ea1ec1cb675ce3b}`