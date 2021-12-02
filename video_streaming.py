import cv2
from flask import *
import requests
import os
RESULT_FOLDER = os.path.join('static', 'result')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = RESULT_FOLDER
cap = cv2.VideoCapture('sample.mp4')
ret, frame = cap.read()
def samplevideo():
    list_data = []
    while (True):
        print(ret)
        files = {'image': open('accedent.jpg', 'rb')}
        res = requests.post('http://182.75.117.230:8085/inference', files=files)
        result = res.json()
        list_data.append(result)
        cap.release()
        cv2.destroyAllWindows()
        return result
@app.route('/vdoprocess', methods=['GET','POST'])
def vdoprocess():
    if request.method == 'GET':
        return render_template("vdoprocess_home.html")
    elif request.method == 'POST':
        res=samplevideo()
        print(res)
        return 'res'
if __name__ == '__main__':

    app.run(debug=True,port=50055)