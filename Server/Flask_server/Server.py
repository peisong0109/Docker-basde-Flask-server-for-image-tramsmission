# @Time     : 10/26/2022 08:33 
# @Author   : Peisong Li
# @FileName : Server.py

from flask import request, Flask
import os
# from werkzeug.utils import secure_filename
import time
import base64

os.environ['TZ'] = 'Asia/Shanghai'
time.tzset()
app = Flask(__name__)



@app.route('/')
def hello_world():
    return 'Hey, we have Flask in a Docker container!'


@app.route("/upload", methods=['POST', 'GET'])
def get_frame():
    if request.method == 'POST':
        # 解析图片数据
        # img = base64.b64decode(str(request.form['file1']))
        # img=str(request.form['file1'])
        file = request.files['file']
        name = file.filename
        file.save(name)        
        # file.save('test.png')
        return {'sim': "0.8"}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=6666)
