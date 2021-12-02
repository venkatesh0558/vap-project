import requests
import cv2
from video_streaming import *
def search_object_api(file=None):
    print("hello")
    files = {'image': open(file, 'rb')}

    res = requests.post('http://182.75.117.230:8085/inference',files=files)
    result=res.json()
    # print(res.json())
    return result
