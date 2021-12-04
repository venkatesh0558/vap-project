from flask import *
import sample
app = Flask(__name__)

def get_search_data(RectA_data, RectB_data,label):
    video_metadata = RectA_data
    # print(video_metadata)
    print(label)
    rectB = RectB_data

    RectB_left = rectB['region'][0]['left']
    RectB_width = rectB['region'][0]['width']
    RectB_top = rectB['region'][0]['top']
    RectB_height = rectB['region'][0]['height']

    list_search_data = []
    for i in video_metadata:
        # print(label)
        if i['label'] == label:
            if (i['left'] <= RectB_left <= i['left'] + RectB_width or RectB_left <= i[
                'left'] <= RectB_left + RectB_width) and (
                    i['top'] <= RectB_top <= i['top'] + i['height'] or RectB_top <= i['top'] <= RectB_top + RectB_height):
                # print(True)
                # print(i)
                list_search_data.append(i)
        else:
            pass

    return list_search_data


@app.route('/search_metadata', methods=['GET','POST'])
def seach_object():
    if request.method == 'POST':
        in_json=request.json
        print(type(in_json))
        video_metadata=sample.video_data(video_id=in_json['Video_id'])
        # print(video_metadata)
        label = in_json['object_arr'][0]
        # print(label)
        res = get_search_data(video_metadata, in_json,label)
        print(res)
        return jsonify(res)

if __name__ == '__main__':

    app.run(debug=True,port=20088)