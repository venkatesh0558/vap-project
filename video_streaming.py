import cv2
from flask import *
import requests
import os
from datetime import datetime as dt
RESULT_FOLDER = os.path.join('static', 'result')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = RESULT_FOLDER
# print("Starting time start====>",dt.now())
cap = cv2.VideoCapture('sample.mp4')
def samplevideo():
    list_data = []
    while (cap.isOpened()):
        ret, frame = cap.read()
        print("API Req timestamp====>", dt.now())
        files = {'image': open('accedent.jpg', 'rb')}
        res = requests.post('http://182.75.117.230:8085/inference', files=files)
        print("API respond timestamp====>", dt.now())
        result = res.json()
        list_data.append(result)
    cap.release()
    cv2.destroyAllWindows()
    return list_data
@app.route('/vdoprocess', methods=['GET','POST'])
def vdoprocess():
    if request.method == 'GET':
        return render_template("vdoprocess_home.html")
    elif request.method == 'POST':
        res=samplevideo()
        return res
if __name__ == '__main__':

    app.run(debug=True,port=50055)