# @Time     : 10/26/2022 08:33 
# @Author   : Peisong Li
# @FileName : Client.py

import requests

file_path1 = 'test.jpg'  # 图片路径
img = open(file_path1, 'rb')
res = {"file": img}
# Access the cloud server with your flask-based cloud server's IP and port.
res = requests.post("http://47.243.109.255:6666/upload", files=res)
print(res.text)

