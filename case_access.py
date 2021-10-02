from functools import wraps
from flask import *
import jwt
import casesDB
import json

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
            current_user  = casesDB.user_verified(data=data)
            print(current_user)
        except:
            return jsonify({
                'message' : 'Token is invalid !!'
            }), 401
        #
        return f(current_user,clientdata, *args, **kwargs)
    return decorated

@app.route('/cases/list', methods=['GET'])
# @authorize
def usercasesget():
    if request.method == 'GET':
        # print(clientdata)
        # print(current_user)
        user_name="kishan"
        res=casesDB.user_get(user_name)
        print(res)
        # print(json.dumps(res))
        # res_json=json.loads(res)
        res_data={"respond":res}
        return jsonify(res_data)

@app.route('/case/active', methods=['GET'])
@authorize
def useractive(urrent_user,clientdata, *args, **kwargs):
    if request.method == 'GET':
        res_data = {"respond": True}
        return res_data


@app.route('/case/deactive', methods=['GET'])
@authorize
def userdeactive(urrent_user,clientdata, *args, **kwargs):
    if request.method == 'GET':
        res_data = {"respond": False}
        return res_data

if __name__ == '__main__':

    app.run(debug=True,port=50022)