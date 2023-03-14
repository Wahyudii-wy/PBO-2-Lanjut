# NIM     : 210511076
# Nama    : Wahyudi
# Kelas   : TIF21B (R2)
      
class Fahrenheit:
    def __init__(self, fahrenheit):
        self.fahrenheit = fahrenheit
    
    def to_celcius(self):
        return (self.fahrenheit - 32) * 5/9
    
    def to_reamur(self):
        return (self.fahrenheit - 32) * 4/9
    
    def to_kelvin(self):
        return (self.fahrenheit + 459.67) * 5/9
    




class Reamur:
    def __init__(self, reamur):
        self.reamur = reamur
    
    def to_celcius(self):
        return self.reamur * 5/4
    
    def to_fahrenheit(self):
        return self.reamur * 9/4 + 32
    
    def to_kelvin(self):
        return self.reamur * 5/4 + 273.15


class Kelvin:
    def __init__(self, kelvin):
        self.kelvin = kelvin
    
    def to_celcius(self):
        return self.kelvin - 273.15
    
    def to_fahrenheit(self):
        return self.kelvin * 9/5 - 459.67
    
    def to_reamur(self):
        return (self.kelvin - 273.15) * 4/5

# Pemanggilan class

suhu = Fahrenheit(60)
celcius = suhu.to_celcius()
reamur = suhu.to_reamur()
kelvin = suhu.to_kelvin()

print(f"{suhu.fahrenheit} derajat Fahrenheit = {kelvin} derajat Kelvin")
print(f"{suhu.fahrenheit} derajat Fahrenheit = {reamur} Reamur")
print(f"{suhu.fahrenheit }derajat Fahrenheit = {celcius} derajat Celcius")   






