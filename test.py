def get_search_data(RectA_data, RectB_data,label):
    video_metadata = RectA_data
    rectB = RectB_data

    RectB_left = rectB['left']
    RectB_width = rectB['width']
    RectB_top = rectB['top']
    RectB_height = rectB['height']

    list_search_data = []

    for i in video_metadata:
        # print(i['label'])
        # print(label)
        if i['label'] == label:
            if (i['left'] <= RectB_left <= i['left'] + RectB_width or RectB_left <= i[
                'left'] <= RectB_left + RectB_width) and (
                    i['top'] <= RectB_top <= i['top'] + i['height'] or RectB_top <= i['top'] <= RectB_top + RectB_height):
                # print(True)
                # print(i)
                list_search_data.append(i)
            #
            # else:
            #     pass
            #
    return list_search_data
