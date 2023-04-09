class Penulis:
    def __init__(self, nama, alamat):
        self.nama = nama
        self.alamat = alamat
        self.buku = []
    
    def tambah_buku(self, judul):
        self.buku.append(Buku(judul))
        
    def info(self):
        print(f"Nama Penulis: {self.nama}")
        print(f"Alamat: {self.alamat}")
        print("Buku yang ditulis:")
        for buku in self.buku:
            print("- " + buku.judul)
        print()
        

class Buku:
    def __init__(self, judul):
        self.judul = judul
    
    def info(self):
        print(f"Judul Buku: {self.judul}")


# membuat objek Penulis
penulis1 = Penulis("Raditya Dika", "Indonesia")
penulis2 = Penulis("Wira Nagara", "Indonesia")
penulis3 = Penulis("Oda ichiro", "Jepang")

# menambahkan beberapa buku untuk penulis
penulis1.tambah_buku("Koala Kumal")
penulis1.tambah_buku("Cinta Brontosaurus")
penulis1.tambah_buku("Manusia Setengah Salmon")
penulis2.tambah_buku("Destilasi Alkena")
penulis3.tambah_buku("One Piece")

# menampilkan informasi Penulis dan Buku
penulis1.info()
penulis2.info()
penulis3.info()