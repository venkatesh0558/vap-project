# video_metadata=[{"label":"person","top":299,"width":116,"left":71,"height":269,"score":0.910591},{"label":"person","top":320,"width":83,"left":5,"height":270,"score":0.881897},{"label":"person","top":301,"width":88,"left":223,"height":263,"score":0.788411},{"label":"car","top":311,"width":418,"left":208,"height":242,"score":0.683376},{"label":"car","top":341,"width":60,"left":179,"height":77,"score":0.679143},{"label":"car","top":311,"width":99,"left":549,"height":73,"score":0.282798},{"label":"car","top":320,"width":109,"left":194,"height":156,"score":0.268574},{"label":"car","top":318,"width":191,"left":429,"height":75,"score":0.208723},{"label":"traffic light","top":170,"width":48,"left":883,"height":49,"score":0.595208},{"label":"backpack","top":343,"width":62,"left":97,"height":61,"score":0.333726},{"label":"handbag","top":403,"width":34,"left":211,"height":93,"score":0.216817},{"label":"suitcase","top":275,"width":100,"left":826,"height":43,"score":0.228349}]


# from collections import Counter
# tokens = [{"Value": "Blah", "SO": 0}, {"Value": "zoom", "SO": 5}, {"Value": "Blah", "SO": 2}, {"Value": "Blah", "SO": 3}]
# res=Counter(tok['label'] for tok in video_metadata)
# print(dict(res))
def video_data(video_id=None):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.videoDB
    cur_data=[]
    for i in db.video_api.find({'Video_id':str(video_id)}):
        # print(type(i.get('video_frame_data')))
        len_objects=len(i.get('video_frame_data'))
        if len_objects >0:
            cur_data.append(i['video_frame_data'])
    # print(len(cur_data))
    flat_list = [item for sublist in cur_data for item in sublist]
    # print(len(flat_list))
    res_data=[]
    for i in flat_list:
        if type(i) is dict:
            res_data.append(i)
        else:
            pass
    return res_data
# res=video_data(video_id=)
# print(len(res))