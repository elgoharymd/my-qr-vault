import qrcode
import os

# المسارات
upload_dir = 'uploads/'
qr_dir = 'qrcodes/'

if not os.path.exists(qr_dir):
    os.makedirs(qr_dir)

# رابط GitHub Pages الخاص بك
base_url = "https://elgoharymd.github.io/my-qr-vault/uploads/"

for filename in os.listdir(upload_dir):
    # نتأكد من أنه ملف وليس مجلد
    if os.path.isfile(os.path.join(upload_dir, filename)):
        # إنشاء الرابط المباشر
        file_url = base_url + filename
        
        # إنشاء الـ QR Code
        qr = qrcode.make(file_url)
        qr_save_path = os.path.join(qr_dir, f"{filename}.png")
        qr.save(qr_save_path)
        print(f"Generated QR for: {filename}")
