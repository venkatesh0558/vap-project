
# def search_dictionaries(value):
#     sample_data = [{"label": "person", "top": 10, "width": 198, "left": 948, "height": 393, "score": 0.7},
#                    {"label": "person", "top": 15, "width": 234, "left": 210, "height": 282, "score": 0.65},
#                    {"label": "person", "top": 737, "width": 111, "left": 80, "height": 256, "score": 0.45},
#                    {"label": "car", "top": 737, "width": 111, "left": 80, "height": 256, "score": 0.45},
#                    {"label": "truck", "top": 737, "width": 111, "left": 80, "height": 256, "score": 0.45}]
#
#     return [element for element in sample_data if value in element.values()]
# res=search_dictionaries('person')
# print(res)
# def sampledec(value):
#     sample_data = [{"label": "person", "top": 10, "width": 198, "left": 948, "height": 393, "score": 0.7},
#                    {"label": "person", "top": 15, "width": 234, "left": 210, "height": 282, "score": 0.65},
#                    {"label": "person", "top": 737, "width": 111, "left": 80, "height": 256, "score": 0.45},
#                    {"label": "Car", "top": 737, "width": 111, "left": 80, "height": 256, "score": 0.45},
#                    {"label": "Truck", "top": 737, "width": 111, "left": 80, "height": 256, "score": 0.45}]
#
#     list_of_all_values = [value for elem in sample_data
#                       for value in elem.values()]
#     print(list_of_all_values)
#     return list_of_all_values
# res=sampledec("Car")
# print(res)

# def search_objectIn_json(in_json):
#     print(in_json)
#     list_metadata=in_json
#
#     value_list=list_metadata['object_arr']
#     print(value_list)
#     value=value_list[0]
#     print(type(value))
#
#     video_metadata = [{"label": "person", "top": 10, "width": 198, "left": 948, "height": 393, "score": 0.7},
#                    {"label": "person", "top": 15, "width": 234, "left": 210, "height": 282, "score": 0.65},
#                    {"label": "person", "top": 737, "width": 111, "left": 80, "height": 256, "score": 0.45},
#                    {"label": "car", "top": 737, "width": 111, "left": 80, "height": 256, "score": 0.45},
#                    {"label": "truck", "top": 737, "width": 111, "left": 80, "height": 256, "score": 0.45}]
#
#     return [element for element in video_metadata if value in element.values()]

def dsearch(lod, **kw):

    return filter(lambda i: all((i[k] == v for (k, v) in kw.items())), lod)


def search_objectIn_json_data(in_json):
    print(in_json)
    list_metadata=in_json

    value_list=list_metadata['object_arr']
    print(value_list)
    value=value_list[0]
    print(type(value))
    reg_list=list_metadata['region']
    print(reg_list)
    top=reg_list[0]['top']
    left=reg_list[0]['left']
    width=reg_list[0]['width']
    height=reg_list[0]['height']
    video_metadata = [{"label": "person", "top": 10, "width": 198, "left": 948, "height": 393, "score": 0.7},
                   {"label": "person", "top": 15, "width": 234, "left": 210, "height": 282, "score": 0.65},
                   {"label": "person", "top": 737, "width": 111, "left": 80, "height": 256, "score": 0.45},
                   {"label": "car", "top": 737, "width": 111, "left": 80, "height": 256, "score": 0.45},
                   {"label": "truck", "top": 737, "width": 111, "left": 80, "height": 256, "score": 0.45}]
    res_metadata = list(dsearch(video_metadata, label=value, top=top, width=width, left=left, height=height))

    return res_metadata


