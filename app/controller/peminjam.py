from flask_restful import Resource
from flask import request
from app import app, db
from datetime import datetime, timedelta
from flask_jwt_extended import jwt_required


class DaftarPeminjam(Resource):
    @jwt_required
    def get(self):
        """
        Mengeluarkan peminjam
        """
        sql = """select * from peminjam"""
        return db.get_data(sql,[])

class TambahPeminjam(Resource):
    @jwt_required
    def post(self):
        now = datetime.now()
        stor = now + timedelta(days=3)
        data = request.get_json()
        sql = """insert peminjam values (0,%s,%s,%s,%s,%s)"""
        params = [data["nama"],data["buku"],stor,now,now]
        return db.commit_data(sql,params)

class UpdatePeminjam(Resource):
    @jwt_required
    def get(self,id):
        sql = """select * from peminjam where id = %s"""
        return db.get_one(sql,[id])
    @jwt_required
    def put(self,id):
        now = datetime.now()
        data = request.get_json()
        sql = """update peminjam set nama = %s, buku = %s, created_at = %s, updated_at = %s"""
        params = [data["nama"], data["buku"], now, now]
        return db.commit_data(sql,params)

class HapusPeminjam(Resource):
    @jwt_required
    def delete(self,id):
        sql = """delete from peminjam where id = %s"""
        return db.commit_data(sql,[id])