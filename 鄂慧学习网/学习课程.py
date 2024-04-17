import random
import time

import requests

url = "https://api.hubei21.com/api/video_detail_study"
token = "c53e95b5246eadaddd2962ab3795fdb7"
headers = {
    "token": token,
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15",
    "Content-Type": "application/json"
}
random_number = random.randint(3000, 5000)  # 生成随机的播放时间
data = {
    "video_id": 12,
    "video_detail_id": 0,
    "ratio": "100.00",
    "time": random_number
}

for i in range(55, 73):  # 一次刷完所有课程
    # 停顿2s
    time.sleep(1)
    data["video_detail_id"] = i
    response = requests.post(url, headers=headers, json=data)
    print(response.text)
