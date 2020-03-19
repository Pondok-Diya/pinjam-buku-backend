from flask_restful import Resource
from flask import request
from app import app, db
from datetime import datetime, timedelta
from flask_jwt_extended import jwt_required


exp = timedelta(days=3)

def checkAnggota(id):
    sql = """select * from anggota where id = %s"""
    res =  db.get_one(sql,[id])
    return res

def checkBuku(kode):
    sql = """select * from list_buku where kode = %s"""
    res = db.get_one(sql,[kode])
    return res

def checkPengembalian(id):
    sql = """select waktu_pengembalian from peminjam where id = %s"""
    res = db.get_one(sql,[id])
    hasil = datetime.now() - res['waktu_pengembalian']
    return hasil

class DaftarPeminjam(Resource):
    @jwt_required
    def get(self):
        """
        Mengeluarkan peminjam
        """
        sql = """select peminjam.id, anggota.nama, list_buku.judul, peminjam.created_at, waktu_pengembalian from peminjam join list_buku on peminjam.kode_buku = list_buku.kode join anggota on anggota.id = peminjam.no_anggota"""
        return db.get_data(sql,[])

class TambahPeminjam(Resource):
    @jwt_required
    def post(self):
        now = datetime.now()
        stor = now + exp
        data = request.get_json()
        if checkAnggota(int(data['no_anggota'])) == None and checkBuku(data['kode_buku']) == None:
            return {'msg': 'Nomor anggota atau kode buku yang anda masukkan tidak terdaftar'}
        sql = """insert peminjam values (0,%s,%s,%s,%s,%s)"""
        params = [int(data["no_anggota"]),data["kode_buku"],stor,now,now]
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
        if checkPengembalian(id) > exp:
            hasil = db.commit_data(sql,[id])
            hasil['msg'] = 'Denda Rp.3000.00'
            return hasil
        return db.commit_data(sql,[id])