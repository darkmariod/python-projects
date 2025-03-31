import qrcode

data = "https://tu-link-aqui.com"

qr = qrcode.make(data)

qr.save("cv_qr.png")


print("Codigo QR generado correctamente como 'cv_qr.png'")