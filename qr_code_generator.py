import qrcode

data = input('Enter the text or URL: ').strip()
filename = input('Enter the filename: ').strip()

# Create the QR code object
qr = qrcode.QRCode(box_size=10, border=4)

# Add the data (Only need to do this once)
qr.add_data(data)

# Create and save the image
image = qr.make_image(fill_color="black", back_color="white")
image.save(filename)

print(f'QR code saved as {filename}')