import qrcode
import os

# المسار الذي يحتوي على الملفات المرفوعة
upload_dir = 'uploads/'
qr_dir = 'qrcodes/'

# التأكد من وجود مجلد الـ QR
if not os.path.exists(qr_dir):
    os.makedirs(qr_dir)

for filename in os.listdir(upload_dir):
    if filename.endswith((".mp3", ".wav", ".m4a")):
        # إنشاء الرابط المباشر للملف على GitHub Pages
        # استبدل USERNAME و REPO باسم حسابك ومستودعك
        file_url = f"https://USERNAME.github.io/REPO/uploads/{filename}"
        
        # إنشاء الـ QR Code
        qr = qrcode.make(file_url)
        qr_save_path = os.path.join(qr_dir, f"{filename}.png")
        qr.save(qr_save_path)
        print(f"Generated QR for {filename}")
