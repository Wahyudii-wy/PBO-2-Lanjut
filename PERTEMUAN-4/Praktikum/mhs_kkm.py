class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
    
    def info(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        

class Kelompok:
    def __init__(self, nomor, anggota=[]):
        self.nomor = nomor
        self.anggota = anggota
        
    def tambah_anggota(self, mhs):
        self.anggota.append(mhs)
        
    def info(self):
        print(f"Kelompok {self.nomor}")
        print("Daftar Anggota:")
        for mhs in self.anggota:
            mhs.info()
        print()

# membuat beberapa objek Mahasiswa
mhs1 = Mahasiswa("Vita", "210511000")
mhs2 = Mahasiswa("Della", "210511001")
mhs3 = Mahasiswa("Malika", "210511002")
mhs4 = Mahasiswa("Wali", "210511003")


# membuat beberapa objek Kelompok dan menambahkan anggotanya
kel1 = Kelompok("KKM 1")
kel1.tambah_anggota(mhs1)
kel1.tambah_anggota(mhs2)

kel2 = Kelompok("KKM 2")
kel2.tambah_anggota(mhs3)
kel2.tambah_anggota(mhs4)

# menampilkan informasi kelompok dan anggotanya
kel1.info()
kel2.info()
