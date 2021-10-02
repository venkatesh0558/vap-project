from functools import wraps
from flask import *
import jwt
import casesDB
import json
app = Flask(__name__)

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
def create():
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
if __name__ == '__main__':

    app.run(debug=True,port=50066)