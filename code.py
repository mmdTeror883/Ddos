import os
import platform
import time

def ping_site(ip):
    # تعیین دستور پینگ بر اساس سیستم عامل
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '4', ip]

    # اجرای دستور پینگ
    start_time = time.time()
    response = os.system(' '.join(command))
    end_time = time.time()

    # بررسی پاسخ
    if response == 0:
        print(f"سایت {ip} در دسترس است.")
        print(f"زمان پاسخ: {end_time - start_time:.2f} ثانیه")
    else:
        print(f"سایت {ip} در دسترس نیست.")

# آدرس IP سایت را وارد کنید
ip_address = input("لطفاً آدرس IP سایت را وارد کنید: ")
ping_site(ip_address)
