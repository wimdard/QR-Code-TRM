import qrcode
import os


data = input("Введите данные для QR-кода (например, URL): ")
data_name = input("Введите имя QR-Code: ")


downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
data_name = os.path.join(downloads_folder, f"{data_name}.png")


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)


qr.add_data(data)
qr.make(fit=True)


img = qr.make_image(fill_color="black", back_color="white")


img.save(f"{data_name}.png")

print("QR-код сохранен как 'qrcode.png'")
