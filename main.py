import cv2
import requests

cap = cv2.VideoCapture('sample.mp4')
def samplevideo():
    list_data = []
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            cv2.imshow('frame',frame)
            files = {'image': open('accedent.jpg', 'rb')}
            res = requests.post('http://182.75.117.230:8085/inference', files=files)
            result = res.json()
            list_data.append(result)


        else:
            cv2.destroyAllWindows()
        cap.release()

    return list_data
res=samplevideo()
print(res)