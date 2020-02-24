from flask_restful import Resource
from flask import request
from app import app, db
from datetime import datetime, timedelta
from passlib.hash import pbkdf2_sha256 as sha256
from flask_jwt_extended import create_access_token

def checkingUser(user):
    sql = """select * from user where username=%s"""
    params = [user]
    res = db.get_one(sql,params)
    return res

def verify_hash(password,hash):
    return sha256.verify(password,hash)

class Registrasi(Resource):
    def post(self):
        datetime_now = datetime.now()
        data = request.get_json()
        try:
            if checkingUser(data["username"]) == None:
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
        user = checkingUser(data["username"])
        try:
            if user != None:
                if verify_hash(data["password"],user["password"]):
                    access_token = create_access_token(identity=data["username"],expires_delta=timedelta(hours = 6))
                    return {
                        "access_token":access_token,
                        "user":user["username"]
                    }
            return {
                "msg":"user or password wrong"
            }, 403
        except Exception as e:
            app.logger.error(e)
            return {"msg":"ups, something wrong"}