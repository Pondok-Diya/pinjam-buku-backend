from app import api
from app.controller.buku import DaftarBuku, TambahBuku, UpdateBuku, HapusBuku
from app.controller.anggota import Anggota, DaftarAnggota, HapusAnggota
from app.controller.peminjam import DaftarPeminjam, TambahPeminjam, UpdatePeminjam, HapusPeminjam
from app.controller.user import Registrasi, Login

api.add_resource(DaftarBuku,'/buku')
api.add_resource(TambahBuku,'/buku/tambah')
api.add_resource(UpdateBuku,'/buku/<id>')
api.add_resource(HapusBuku,'/buku/hapus/<id>')
api.add_resource(DaftarAnggota,'/anggota')
api.add_resource(Registrasi,'/registrasi')
api.add_resource(Login,'/login')
api.add_resource(Anggota,'/anggota/<id>')
api.add_resource(HapusAnggota,'/anggota/hapus/<id>')
api.add_resource(DaftarPeminjam,'/peminjam')
api.add_resource(TambahPeminjam,'/peminjam/tambah')
api.add_resource(UpdatePeminjam,'/peminjam/<id>')
api.add_resource(HapusPeminjam,'/peminjam/hapus/<id>')