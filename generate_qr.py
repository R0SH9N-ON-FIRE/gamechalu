import qrcode

url = "https://your-hosted-url.com"  # Replace with your actual hosted link
qr = qrcode.make(url)
qr.save("roshan_qr.png")
print("✅ QR code saved as roshan_qr.png")
