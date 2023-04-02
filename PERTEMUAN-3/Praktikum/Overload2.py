class Kambing:
    def __init__(self, nama, usia):
        self.nama = nama
        self.usia = usia

    def info(self):
        print(f"Saya adalah kambing. nama saya {self.nama}. umur saya {self.usia} tahun.")

    def make_sound(self):
        print("Mbeeek")


class Buaya:
    def __init__(self, nama, usia):
        self.nama = nama
        self.usia = usia

    def info(self):
        print(f"Saya adalah Buaya. nama saya {self.nama}. umur saya {self.usia} tahun.")

    def make_sound(self):
        print("Hallo dek, udah makan belom?")


kambing = Kambing("Asep", 2)
buaya = Buaya("Riski", 17)

for animal in (kambing, buaya):
    animal.info()
    animal.make_sound()
