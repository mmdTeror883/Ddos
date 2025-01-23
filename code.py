from flask import Flask, request
from collections import defaultdict

app = Flask(__name__)

# دیکشنری برای شمارش درخواست‌ها از هر IP
request_count = defaultdict(int)

@app.route('/')
def index():
    ip = request.remote_addr
    request_count[ip] += 1

    # اگر تعداد درخواست‌ها از یک IP خاص بیشتر از 100 باشد، هشدار می‌دهیم
    if request_count[ip] > 100:
        return "Warning: Possible DDoS attack detected from IP: {}".format(ip), 429

    return "Welcome to the site!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
