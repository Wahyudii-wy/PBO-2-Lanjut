# Tugas Praktikum
# NIM     : 210511076
# Nama    : Wahyudi
# Kelas   : TIF21B (R2)

# 2. Buatlah Class yang mengimplementasikan Object Oriented Programming, beri nama: celcius_oop.py

class KonversiSuhu:
    def __init__(self, celcius):
        self.celcius = celcius

    def to_reamur(self):
        return (4/5) * self.celcius

    def to_kelvin(self):
        return self.celcius + 273.15

    def to_fahrenheit(self):
        return (9/5) * self.celcius + 32


suhu = KonversiSuhu(60)
fahrenheit = suhu.to_fahrenheit()
kelvin = suhu.to_kelvin()
reamur = suhu.to_reamur()

print(f"{suhu.celcius} derajat Celsius = {reamur} derajat Reamur")
print(f"{suhu.celcius} derajat Celsius = {kelvin} Kelvin")
print(f"{suhu.celcius} derajat Celsius = {fahrenheit} derajat Fahrenheit")
