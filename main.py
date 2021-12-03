import cv2
import requests
from datetime import datetime as dt

cap = cv2.VideoCapture('sample1.mp4')
def samplevideo():
    list_data = []
    # print("Starting time start====>",dt.now())
    while (cap.isOpened()):
        ret, frame = cap.read()
        print("FPS rate====>",cap.get(cv2.CAP_PROP_FPS))
        print("API Req timestamp====>", dt.now())
        cv2.imwrite('sampletest.jpg',frame)
        files = {'image': open('sampletest.jpg', 'rb')}
        res = requests.post('http://182.75.117.230:8085/inference', files=files)
        print("API respond timestamp====>", dt.now())
        result = res.json()
        print(result)
        list_data.append(result)
    cap.release()
    cv2.destroyAllWindows()
    return list_data
res=samplevideo()
print(res)