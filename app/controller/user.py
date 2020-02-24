from flask_restful import Resource
from flask import request
from app import app, db
from datetime import datetime
from passlib.hash import pbkdf2_sha256 as sha256

def checkingUser(user,email):
    sql = """select username, email from user where username=%s and email=%s"""
    params = [user,email]
    res = db.get_one(sql,params)
    return res

class Registrasi(Resource):
    def post(self):
        datetime_now = datetime.now()
        data = request.get_json()
        try:
            if checkingUser(data["username"],data["email"]) == None:
                sql = """insert user values (0, %s,%s,%s,%s,%s,%s)"""
                params = [data["nama"],data["username"],data["email"],sha256.hash(data["password"]),datetime_now,datetime_now]
                db.commit_data(sql,params)
                return {"msg" : "Sukses"}
            return {"msg":"user exist"}
        except Exception as e:
            app.logger.error(e)
            return {"msg" : "ups, something wrong"}, 500

class Login(Resource):
    def post(self):
        data = request.get_json()
        sql = """select * from user where username=%s"""
        params = [data["username"]]
        password = db.get_one(sql,params)
        print(password)
        if sha256.verify(data["password"],password["password"]):
            return {"msg":"login"}
        else:
            return {"msg":"password yang anda masukkan salah"}
        