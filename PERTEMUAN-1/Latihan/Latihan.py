#Konversi Suhu Celcius Ke Fahrenheit, Reamur, dan Kelvin:
# C = 75
# F = (9/5) * C + 32
# print("konversi ",C, "derajat celcius adalah ",F, "derajat fahrenheit")

# Konversi Suhu Celcius Ke Reamur:
# C = 60
# R = 4/5 * C
# print("konversi ",C, "derajat celcius adalah ",R, "derajat Reamur")

# Konversi Suhu Celcius Ke Kelvin:
# C = 90
# K = C + 273
# print("konversi ",C, "derajat celcius adalah ",K, "derajat Kelvin")

class KonversiSuhu:
    @staticmethod
    def celsius1_to_fahrenheit(celsius):
        return (9/5) * celsius1 + 32

    @staticmethod
    def celsius2_to_reamur(celsius):
        return (4/5) * celsius2

    @staticmethod
    def celsius3_to_kelvin(celsius):
        return celsius3 + 273.15

# Contoh penggunaan
celsius1 = 75
celsius2 = 60
celsius3 = 90

fahrenheit = KonversiSuhu.celsius1_to_fahrenheit(celsius1)
reamur = KonversiSuhu.celsius2_to_reamur(celsius2)
kelvin = KonversiSuhu.celsius3_to_kelvin(celsius3)

print("konversi",celsius1, "derajat celcius adalah ",fahrenheit, "derajat fahrenheit")
print("konversi",celsius2, "derajat celcius adalah ",reamur, "derajat Reamur")
print("konversi",celsius3, "derajat celcius adalah ",kelvin, "derajat Kelvin")