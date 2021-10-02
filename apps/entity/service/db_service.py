from db_access import *
import json
import bcrypt


db = client.VAP # create local UserEntity database on the fly

def entity_insert(data=None):

    print(data)
    db.entity.insert(data)
    return "Entity registered"

def entity_get():

    cur = db.entity.find({}, {"_id": 0})
    cur_list = []
    for i in cur:
        # print(i)
        cur_list.append(i)
    res = json.dumps(cur_list)
    return res
def entity_update(data=None):
    Corporate_Email_Address=data['Corporate_Email_Address']
    print(Corporate_Email_Address)
    print(data['updatedata'])
    db.entity.update_one({"Corporate_Email_Address":str(Corporate_Email_Address)},{"$set":data['updatedata']})
    return "Updated Entity"

def user_insert(data=None):

    print(data)
    hashpass = bcrypt.hashpw(data['Password'].encode('utf-8'), bcrypt.gensalt())
    data['Password']=hashpass
    db.user.insert(data)
    return "user has created"

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

def user_get():
    cur = db.user.find({}, {"_id": 0})
    cur_list = []
    for i in cur:
        # print(i)
        i['Password']=i['Password'].decode()
        cur_list.append(i)
    # res = json.dumps(cur_list)
    return cur_list
def user_delete(data=None):

    delete_data = db.user.delete_one(data)
    print(delete_data)
    return "User Deleted"
def user_update(data=None):
    Email_Address=data['Email_Address']
    db.user.update_one({"Email_Address":str(Email_Address)},{"$set":data['updatedata']})
    return "User Updated"