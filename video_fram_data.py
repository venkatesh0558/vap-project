import cv2
import requests
import base64
from datetime import datetime as dt
from pymongo import *
client = MongoClient('localhost:27017')
db=client.videoDB
cap = cv2.VideoCapture('sample1.mp4')
def samplevideo():
    list_data = []
    # print("Starting time start====>",dt.now())
    while (cap.isOpened()):
        ret, frame = cap.read()
        print("FPS rate====>",cap.get(cv2.CAP_PROP_FPS))
        print("API Req timestamp====>", dt.now())
        cv2.imwrite('sampletest1.jpg',frame)
        files = {'image': open('sampletest1.jpg', 'rb')}
        # res = requests.post('http://182.75.117.230:8085/inference', files=files)
        # print("API respond timestamp====>", dt.now())
        # result = res.json()
        # print(result)
        with open('sampletest1.jpg', 'rb') as imgFile:
            image = base64.b64encode(imgFile.read())
            # db.tesing.insert_one({'frame_data':image})
            data={'Video_id':'sample_anupama',
                  'Timestamp':str(dt.now()),
                  'video_name':'sample1.mp4',
                  'image_data':image
                  }
            db.video_frame_data.insert(data)
        # list_data.append(result)
    cap.release()
    cv2.destroyAllWindows()
    return list_data
res=samplevideo()
print(res)