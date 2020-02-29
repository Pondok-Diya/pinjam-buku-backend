from flask_restful import Resource
from flask import request
from app import app, db
from datetime import datetime
from flask_jwt_extended import jwt_required


class DaftarBuku(Resource):
    @jwt_required
    def get(self):
        """
        Mengeluarkan buku
        """
        sql = """select * from list_buku"""
        return db.get_data(sql,[])

class TambahBuku(Resource):
    @jwt_required
    def post(self):
        """
        Menambahkan buku
        """
        now = datetime.now()
        data = request.get_json()
        sql = """insert into list_buku values(0,%s,%s,%s,%s,%s,%s,%s)"""
        params = [data["judul"],data["genre"],data["penulis"],data["penerbit"],data["isbn"],now,now]
        return db.commit_data(sql,params)

class UpdateBuku(Resource):
    @jwt_required
    def get(self,id):
        sql = """select * from list_buku where id = %s"""
        return db.get_one(sql,[id])
    @jwt_required
    def put(self,id):
        """
        Mengganti buku
        """
        data = request.get_json()
        sql = """update list_buku set judul = %s, genre = %s, penulis = %s, penerbit = %s, isbn = %s, updated_at = %s where id = %s"""
        params = [data["judul"],data["genre"],data["penulis"],data["penerbit"],data["isbn"],datetime.now(),id]
        return db.commit_data(sql,params)
class HapusBuku(Resource):
    @jwt_required
    def delete(self,id):
        """
        Menghapus buku
        """
        sql = """delete from list_buku where id = %s"""
        return db.commit_data(sql,[id])