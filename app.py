from functools import wraps
from flask import *
import jwt
import datetime
import os
from apps.entity.service.db_service import *
import json
import casesDB
import media_meatadata
from videodb import video_metadata_insert
app = Flask(__name__)

def authorize(f):
    @wraps(f)

    def decorated(*args, **kwargs):
        token = None
        clientdata=request.json
        # jwt is passed in the request header
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401

        try:
            # print(token)
            token_apikey = token.split(' ')
            data = jwt.decode(token_apikey[1], "secret", algorithm="HS256")
            # print(data)
            current_user  = user_verified(data=data)
            print(current_user)
        except:
            return jsonify({
                'message' : 'Token is invalid !!'
            }), 401
        #
        return f(current_user,clientdata, *args, **kwargs)
    return decorated
@app.route('/entity/create', methods=['POST'])
def create():

    if request.method == 'POST':
        entity_data=request.json
        names = ('Organization_Name', 'Corporate_Email_Address','Entity_Status')
        re_dataset=set(names).issubset(entity_data)
        print(re_dataset)
        try:
            if re_dataset is True:
                    res=entity_insert(data=entity_data)
                    print(res)
                    return res
            else:
                return "Something missing your entity fields"
        except:
            return "something wrong please try again"

@app.route('/entity/get', methods=['GET'])
def getdata():
    if request.method == 'GET':
        res=entity_get()
        print(res)
        res_json=json.loads(res)
        res_data={"respond":res_json}
        return res_data

@app.route('/entity/update', methods=['PUT'])
def updatedata():

    if request.method == 'PUT':
        entity_data = request.json
        names = ('Corporate_Email_Address', 'updatedata')
        re_dataset = set(names).issubset(entity_data)
        print(re_dataset)
        try:
            if re_dataset is True:
                res = entity_update(data=entity_data)
                print(res)
                return res
            else:
                return "Something missing your entity update fields"
        except:
            return "something wrong please try again"

@app.route('/entity/active', methods=['GET'])
def active():
    if request.method == 'GET':
        res_data = {"respond": True}
        return res_data


@app.route('/entity/deactive', methods=['GET'])
def deactive():
    if request.method == 'GET':
        res_data = {"respond": False}
        return res_data

@app.route('/user/create', methods=['POST'])
def user():
    if request.method == 'POST':
        entity_data = request.json
        if entity_data:
            names = ('First_Name', 'Email_Address', 'Login_Id','Password')
            re_dataset = set(names).issubset(entity_data)
            print(re_dataset)
            try:
                if re_dataset is True:
                    res = user_insert(data=entity_data)
                    print(res)
                    return res
                else:
                    return "Something missing your user fields"
            except:
                return "something wrong please try again"
        else:
            return "Please give required data"
@app.route('/user/get', methods=['GET'])
@authorize
def userget(current_user,clientdata, *args, **kwargs):
    if request.method == 'GET':
        print(clientdata)
        print(current_user)
        res=user_get()
        # print(json.dumps(res))
        # res_json=json.loads(res)
        res_data={"respond":res}
        return jsonify(res_data)
@app.route('/user/update', methods=['PUT'])
@authorize
def userupdatedata(urrent_user,clientdata, *args, **kwargs):

    if request.method == 'PUT':
        user_data = request.json
        names = ('Email_Address', 'updatedata')
        re_dataset = set(names).issubset(user_data)
        print(re_dataset)
        try:
            if re_dataset is True:
                res = user_update(data=user_data)
                print(res)
                return res
            else:
                return "Something missing your user update fields"
        except:
            return "something wrong please try again"
@app.route('/user/delete', methods=['DELETE'])
@authorize
def userdeletedata(urrent_user,clientdata, *args, **kwargs):
    if request.method == 'DELETE':
        entity_data=request.json
        print(entity_data)
        res=user_delete(data=entity_data)
        print(res)
        return res
@app.route('/user/active', methods=['GET'])
@authorize
def useractive(urrent_user,clientdata, *args, **kwargs):
    if request.method == 'GET':
        res_data = {"respond": True}
        return res_data


@app.route('/user/deactive', methods=['GET'])
@authorize
def userdeactive(urrent_user,clientdata, *args, **kwargs):
    if request.method == 'GET':
        res_data = {"respond": False}
        return res_data

#----------------Case ----------

@app.route('/cases/list', methods=['GET'])
def casesget():
    if request.method == 'GET':
        # print(clientdata)
        res=casesDB.get_all_cases_user()
        # print(json.dumps(res))
        # res_json=json.loads(res)
        res_data={"respond":res}
        return jsonify(res_data)

@app.route('/cases/create', methods=['POST'])
def create1():
    if request.method == 'POST':
        cases_data=request.json
        names = ('Case_No','Case_Status')
        re_dataset=set(names).issubset(cases_data)
        print(re_dataset)
        try:
            if re_dataset is True:
                    res=casesDB.case_create(data=cases_data)
                    print(res)
                    return res,200
            else:
                return "Something missing your case fields"
        except:
            return "something wrong please try again"
@app.route('/cases/all', methods=['GET'])
def casesgetall():
    if request.method == 'GET':
        # print(clientdata)
        res=casesDB.get_all_cases_user()
        # print(json.dumps(res))
        # res_json=json.loads(res)
        res_data={"respond":res}
        return jsonify(res_data)


#----------------- permissions and role ----------------


@app.route('/role/create', methods=['POST'])
def rolecreate():
    if request.method == 'POST':
        entity_data=request.json
        names = ('Role_Name', 'permissions_id',)
        re_dataset=set(names).issubset(entity_data)
        print(re_dataset)
        try:
            if re_dataset is True:
                    # res= mongo_rp.entity_insert(data=entity_data)
                    # print(res)
                    return "Done"
            else:
                return "Something missing your data fields, fields must have ('Role_Name', 'permissions_id',)"
        except:
            return "something wrong please try again"

@app.route('/role/list', methods=['GET'])
def rolegetdata():
    if request.method == 'GET':
        # res= mongo_rp.entity_get()
        # print(res)
        # res_json=json.loads(res)
        res_data={"respond":"res_json"}
        return res_data

@app.route('/role/update', methods=['PUT'])
def roleupdate():

    if request.method == 'PUT':
        entity_data = request.json
        names = ('Role_Name', 'updatedata')
        re_dataset = set(names).issubset(entity_data)
        print(re_dataset)
        try:
            if re_dataset is True:
                # res = mongo_rp.entity_update(data=entity_data)
                # print(res)
                return "Role Updated"
            else:
                return "Something missing your entity update fields"
        except:
            return "something wrong please try again"

@app.route('/role/active', methods=['GET'])
def activerole():
    if request.method == 'GET':
        res_data = {"respond": True}
        return res_data


@app.route('/role/deactive', methods=['GET'])
def deactiverole():
    if request.method == 'GET':
        res_data = {"respond": False}
        return res_data
@app.route('/role/assign', methods=['GET'])
def assign():
    if request.method == 'GET':
        res_data = {"respond": False}
        return res_data
@app.route('/role/unassign', methods=['GET'])
def assignrole():
    if request.method == 'GET':
        res_data = {"respond": False}
        return res_data
@app.route('/per/create', methods=['POST'])
def Pemissionsuser():
    if request.method == 'POST':
        entity_data = request.json
        if entity_data:
            names = ('per', 'per_list')
            re_dataset = set(names).issubset(entity_data)
            print(re_dataset)
            try:
                if re_dataset is True:
                    # res = mongo_rp.user_insert(data=entity_data)
                    # print(res)
                    return "res"
                else:
                    return "Something missing your user fields"
            except:
                return "something wrong please try again"
        else:
            return "Please give required data"
# @app.route('/per/list', methods=['GET'])
# def userget(current_user,clientdata, *args, **kwargs):
#     if request.method == 'GET':
#         print(clientdata)
#         print(current_user)
#         res=mongo_rp.user_get()
#         # print(json.dumps(res))
#         # res_json=json.loads(res)
#         res_data={"respond":res}
#         return jsonify(res_data)
# @app.route('/per/update', methods=['PUT'])
# def userupdatedata(urrent_user,clientdata, *args, **kwargs):
#
#     if request.method == 'PUT':
#         user_data = request.json
#         names = ('Email_Address', 'updatedata')
#         re_dataset = set(names).issubset(user_data)
#         print(re_dataset)
#         try:
#             if re_dataset is True:
#                 res = mongo_rp.user_update(data=user_data)
#                 print(res)
#                 return res
#             else:
#                 return "Something missing your user update fields"
#         except:
#             return "something wrong please try again"
# @app.route('/per/delete', methods=['DELETE'])
# def userdeletedata(urrent_user,clientdata, *args, **kwargs):
#     if request.method == 'DELETE':
#         entity_data=request.json
#         print(entity_data)
#         res=mongo_rp.user_delete(data=entity_data)
#         print(res)
#         return res
#

@app.route('/uploadvideo', methods=['GET','POST'])
# @authorize
def upload():
    if request.method == 'GET':
        return render_template("index.html")
    elif request.method == 'POST':
        print("hello")
        print(request.form)
        f = request.files['filename']
        print(f)
        file_name = f.filename
        print(file_name)
        f.save(f.filename)
        timestamp=datetime.datetime.now()
        # samplefile = 'sample_videos/file_example_OGG_480_1_7mg.ogg'
        res_meatadata = media_meatadata.metadatainfo(str(file_name))
        current_user="Rao"
        data={
            "UserName":current_user,
            "Video_ID":current_user+'_1',
            "Timestamp":str(timestamp),
            "Video_Status":"Active",
            "Video_Path":str(os.getcwd()+"\saved_videos/"+file_name),
            "Video_Metadata":res_meatadata
        }
        # print(res_meatadata[2])
        res=video_metadata_insert(data)
        print(res)
        return "Video MetaData Stored into DB"
@app.route('/video/active', methods=['GET'])
@authorize
def useractive1(urrent_user,clientdata, *args, **kwargs):
    if request.method == 'GET':
        res_data = {"respond": True}
        return res_data


@app.route('/video/deactive', methods=['GET'])
@authorize
def userdeactive1(urrent_user,clientdata, *args, **kwargs):
    if request.method == 'GET':
        res_data = {"respond": False}
        return res_data

#-------------VCR Controls-------------

@app.route('/', methods=['GET','POST'])
# @authorize
def home():
    return render_template("home.html")

@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        # print("hello")
        # print(request.form)
        f = request.files['filename']
        # print(f)
        print(request.content_length)
        file_name="copy_of_"+f.filename
        # print(file_name.split())
        f.save(file_name)
        return render_template("2ndtest.html")

@app.route('/video/Pause', methods=['GET'])
@authorize
def useractive2(urrent_user,clientdata, *args, **kwargs):
    if request.method == 'GET':
        res_data = {"respond": True}
        return res_data


@app.route('/video/Stop', methods=['GET'])
@authorize
def userdeactive2(urrent_user,clientdata, *args, **kwargs):
    if request.method == 'GET':
        res_data = {"respond": False}
        return res_data
@app.route('/video/Rew_FF', methods=['GET'])
@authorize
def Rew_FF(urrent_user,clientdata, *args, **kwargs):
    if request.method == 'GET':
        res_data = {"respond": False}
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + "res" + b'\r\n\r\n')

if __name__ == '__main__':

    app.run(debug=True,port=50088)