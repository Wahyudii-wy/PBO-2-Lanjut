import pygame

pygame.init()

# definisikan suara hewan
suara_anjing = pygame.mixer.Sound("Sound/anjing.mp3")
suara_kucing = pygame.mixer.Sound("Sound/kucing.wav")
suara_ayam = pygame.mixer.Sound("Sound/ayam.wav")
suara_banteng = pygame.mixer.Sound("Sound/banteng.mp3")
suara_bebek = pygame.mixer.Sound("Sound/bebek.mp3")
suara_gagak = pygame.mixer.Sound("Sound/gagak.mp3")
suara_kuda = pygame.mixer.Sound("Sound/kuda.mp3")
suara_macan = pygame.mixer.Sound("Sound/macan.mp3")
suara_sapi = pygame.mixer.Sound("Sound/sapi.mp3")
suara_serigala = pygame.mixer.Sound("Sound/serigala.mp3")

# buat daftar hewan dan suara mereka
daftar_hewan = ['Anjing', 'Kucing','Ayam', 'Banteng', 'Bebek' ,'Gagak','Kuda', 'Macan', 'Sapi', 'Serigala']
daftar_suara = [suara_anjing, suara_kucing,suara_ayam, suara_banteng,suara_bebek, suara_gagak, suara_kuda, suara_macan, suara_sapi, suara_serigala]

# buat tampilan window
lebar = 600
tinggi = 400
layar = pygame.display.set_mode((lebar, tinggi))

# buat font untuk tulisan
font = pygame.font.Font(None, 36)

# tampilkan daftar hewan
for i in range(len(daftar_hewan)):
    teks = font.render(daftar_hewan[i], 1, (255, 255, 255))
    layar.blit(teks, (100, 50+i*30))

pygame.display.flip()

# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for i in range(len(daftar_hewan)):
                if y >= 50+i*30 and y <= 80+i*30:
                    daftar_suara[i].play()
