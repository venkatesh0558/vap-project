from pymongo import MongoClient
import json
import bcrypt

client = MongoClient('localhost:27017')

db = client.tesingDB # create local UserEntity database on the fly
data={
    "First_Name":"Rao",
    "Last_Name": "RV",
    "Email_Address": "rao_ap_police@apgov.org",
    "Designation":"SP",
    "Login_Id":"rao",
    "Cases_list":['a','b'],
    "Password":"rao123"
}

cur=db.testing.find({})
for i in cur:
    print(type(i['Cases_list']))