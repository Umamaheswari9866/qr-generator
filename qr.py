import qrcode  

# UPI Payment URL
upi_url = 'upi://pay?pa=maheshwariu179@oksbi&pn=&tr=&am=&cu=INR'

# Generating QR code
img = qrcode.make(upi_url)
img.save("payment_qr.png")
img.show()

print("QR code generated successfully!")
