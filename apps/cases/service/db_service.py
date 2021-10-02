from pymongo import MongoClient
import json
import bcrypt
from db_access import db


def get_all_cases_user():
    case_list_cur = db.cases.find({'Case_Status':'Active'}, {"_id": 0})
    cur_list = []
    for i in case_list_cur:
        print(i)
        cur_list.append(i)
    # res = json.dumps(cur_list)
    return cur_list

def user_get(user_name):
    cur = db.user.find({"Login_Id":user_name}, {"_id": 0})
    cur_list = []
    for i in cur:
        # print(i)
        cur_list.append(i['Cases_list'])
    # res = json.dumps(cur_list)
    return cur_list
def user_verified(data=None):
    # print(data)
    login_user = db.user.find_one({'Login_Id' : data['Login_Id']})
    print(login_user)
    if login_user['Login_Id'] == data['Login_Id']:
        if bcrypt.checkpw(data['Password'].encode('utf-8'), login_user['Password']) == True:
            print('Done')
            return 'success',200
        else:
            return 'Invalid password combination'
    else:
        return 'Invalid username/password combination'

def case_create(data=None):
    db.cases.insert(data)
    return "Case has created",200

def close_case_list(data=None):

    print(data)
    return 200
def get_all_cases():
    case_list_cur = db.cases.find({},{"_id": 0})
    cur_list = []
    for i in case_list_cur:
        print(i)
        cur_list.append(i)
    # res = json.dumps(cur_list)
    return cur_list
