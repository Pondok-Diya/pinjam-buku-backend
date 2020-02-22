from flask_restful import Resource
from flask import request
from app import app, db
from datetime import datetime



class DaftarAnggota(Resource):
    def get(self):
        sql = """select * from anggota"""
        return db.get_data(sql,[])

class Registrasi(Resource):
    def post(self):
        now = datetime.now()
        data = request.get_json()
        sql = """insert anggota values (0, %s, %s, %s, %s)"""
        params = [data["nama"],data["alamat"],data["hp"],now,now]
        return db.commit_data(sql,params)

class Anggota(Resource):
    def get(self,id):
        sql = """select * from anggota where id = %s"""
        return db.get_one(sql,[id])
    def put(self,id):
        data = request.get_json()
        sql = """update anggota set nama = %s, alamat = %s, hp = %s, updated_at = %s"""
        params = [data["nama"],data["alamat"],data["hp"],datetime.now()]
        return db.commit_data(sql,params)

class HapusAnggota(Resource):
    def delete(self,id):
        sql = """delete from anggota where id = %s"""
        return db.commit_data(sql,[id])