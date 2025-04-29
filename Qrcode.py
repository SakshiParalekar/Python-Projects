import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=5)
qr.add_data("https://techpro.licindia.in/esign/eSignResponse?iid=1888180")
qr.make(fit=True)
img=qr.make_image(fill_color="blue",back_color="pink")
img.save("lic.png")
