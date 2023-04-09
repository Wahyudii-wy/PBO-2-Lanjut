class Peneliti:
    def __init__(self, nama, bidang):
        self.nama = nama
        self.bidang = bidang
        self.artikel = []
    
    def tambah_artikel(self, judul, isi):
        artikel_baru = Artikel(judul, isi, self.bidang)
        self.artikel.append(artikel_baru)
    
    def kirim_ke_jurnal(self, jurnal):
        for artikel in self.artikel:
            jurnal.tambah_artikel(artikel)
        self.artikel = []

class Jurnal:
    def __init__(self, nama):
        self.nama = nama
        self.artikel = []
    
    def tambah_artikel(self, artikel):
        self.artikel.append(artikel)
    
    def tampilkan_artikel(self):
        print(f"Jurnal {self.nama}:")
        for artikel in self.artikel:
            print(f"Judul: {artikel.judul}")
            print(f"Isi: {artikel.isi}")
            print(f"Bidang: {artikel.bidang}")
            print("-----------")
            
class Artikel:
    def __init__(self, judul, isi, bidang):
        self.judul = judul
        self.isi = isi
        self.bidang = bidang


peneliti1 = Peneliti("Jane Doe", "Biologi")
peneliti1.tambah_artikel("Penemuan Baru tentang DNA", "Kami menemukan bahwa...")
peneliti1.tambah_artikel("Analisis Terbaru tentang Fungsi Sel-sel Tubuh", "Dalam penelitian ini, kami...")
jurnal1 = Jurnal("Jurnal Biologi")
peneliti1.kirim_ke_jurnal(jurnal1)
jurnal1.tampilkan_artikel()
