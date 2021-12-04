import cv2
# path = 'sampletest.jpg'
# image = cv2.imread(path)
# i={
#         "height": 199,
#         "label": "person",
#         "left": 384,
#         "score": 0.34752,
#         "top": 248.0,
#         "width": 66
#     }
# start_point = (i['left'], int(i['top']))  # top,left
# end_point = (i['width'] + i['left'], i['height'] + int(i['top']))
# color = (255, 0, 0)
# thickness = 2
# cv2.rectangle(image, start_point, end_point, color, thickness)
# cv2.imwrite('cord_out.jpeg',image)

# from pymongo import MongoClient
# import base64
# client = MongoClient('localhost:27017')
# db = client.videoDB
# # with open('sampletest.jpg', 'rb') as imgFile:
# #     image = base64.b64encode(imgFile.read())
# #     db.tesing.insert_one({'frame_data':image})
#
# image_data=db.tesing.find({})
# print(image_data)
# image_res=[]
# for i in image_data:
#     image_res.append(i)
# # print(len(image_res[0]['frame_data']))
# image_data=image_res[0]['frame_data']
# with open("imageToSave.png", "wb") as fh:
#     fh.write(base64.decodebytes(image_data))