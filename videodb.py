from db_access import db

def video_metadata_insert(data=None):

    print(data)
    db.videoinfo.insert(data)
    return "Done"