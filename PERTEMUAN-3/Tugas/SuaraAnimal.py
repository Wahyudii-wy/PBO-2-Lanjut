from playsound import *
import pygame
pygame.init()

class Animal:
    def __init__(self, suara_file):
        self.suara_file = suara_file

    def buat_Suara(self):
        
        pygame.mixer.music.load(self.suara_file)
        pygame.mixer.music.play()

class Anjing(Animal):
    def __init__(self):
        super().__init__('Sound/anjing.mp3')
        
class Bebek(Animal):
    def __init__(self):
        super().__init__('Sound/bebek.mp3')
        
class Ayam(Animal):
    def __init__(self):
        super().__init__('Sound/ayam.wav')
        
class Banteng(Animal):
    def __init__(self):
        super().__init__('Sound/banteng.mp3')
        
class Gagak(Animal):
    def __init__(self):
        super().__init__('Sound/gagak.mp3')
        
class Kucing(Animal):
    def __init__(self):
        super().__init__('Sound/kucing.wav')
        
class Kuda(Animal):
    def __init__(self):
        super().__init__('Sound/kuda.mp3')
        
class Macan(Animal):
    def __init__(self):
        super().__init__('Sound/macan.mp3')
        
class Sapi(Animal):
    def __init__(self):
        super().__init__('Sound/sapi.mp3')

class Serigala(Animal):
    def __init__(self):
        super().__init__('Sound/Serigala.mp3')

        
kelas_hewan = [Anjing(), Bebek(), Ayam(), Banteng(), Gagak(), Kucing(), Kuda(), Macan(), Sapi(), Serigala()]

for hewan in kelas_hewan:
    print(hewan)

    hewan.buat_Suara()
    pygame.time.delay(3000)

pygame.quit()
