import qrcode
from PIL import Image

qr=qrcode.QRCode(version=None, error_correction= qrcode.constants.ERROR_CORRECT_H, box_size=10, border=3, )

data = input("Enter the data to encode in the QR code: ")
img = qrcode.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save(r"C:\Users\Bisma\Desktop\python practice\qrcode.png")
print("Your QR code generated and saved successfully!")