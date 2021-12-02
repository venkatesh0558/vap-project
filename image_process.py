import cv2
import sample
path = 'accedent.jpg'
image = cv2.imread(path)
window_name = 'Image'

for i in sample.video_metadata:
    print(i)
    start_point = (i['left'],int(i['top']))  # top,left
    end_point = ( i['width']+i['left'],i['height']+int(i['top']))
    color = (255, 0, 0)
    thickness = 2
    cv2.rectangle(image, start_point, end_point, color, thickness)
# cv2.rectangle(image, start_point, end_point, color, thickness)

cv2.imwrite('../static/result.jpg',image)
