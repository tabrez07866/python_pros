import qrcode
import qrcode.constants

data=input("Enter text or URL to generate QR code: ")

qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

qr.add_data(data)
qr.make(fit=True)

img=qr.make_image(fill_colot="black",back_color="white")

img.save("qr_code.png")

print("✅ QR Code generated and saved as 'qr_code.png'")