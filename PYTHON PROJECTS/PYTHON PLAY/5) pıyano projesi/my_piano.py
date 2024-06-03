import pygame
import play

enstruman = 0

# arayüz - ipuçları, kontrol düğmeleri:
play.set_backdrop('light blue')
introduce1 = play.new_text(words='Piano for fun!', 
    x=0, y=200)

introduce2 = play.new_text(words='Create your own melody', 
    x=0, y=150)

#play melody butonu
buton_1 = play.new_box(color="light green",
    x=-100,y=-130,border_color="black",border_width=2,
    width=150,height=50)

buton_1_yazi = play.new_text(words="Play Melody",
    x=-100,y=-130,font_size=30)

#clear melody butonu
buton_2 = play.new_box(color="yellow",x=100,y=-130,
    border_color="black",border_width=2,width=150,height=50)

buton_2_yazi = play.new_text(words="Clear Melody",
    x=100,y=-130,font_size=30)

#enstrüman çeşitleri kodlanıyor

daire_p = play.new_circle(color="black",
    x=-180,y=-200,radius=10,border_color="black",border_width=2)

text_p = play.new_text(words="Piyano",
    x=-145,y=-200,font_size=20)

daire_g = play.new_circle(color="light blue",
    x=-80,y=-200,radius=10,border_color="black",border_width=2)

text_g = play.new_text(words="Gitar",
    x=-45,y=-200,font_size=20)

daire_v = play.new_circle(color="light blue",
    x=20,y=-200,radius=10,border_color="black",border_width=2)

text_v = play.new_text(words="Violin",x=55,y=-200,font_size=20)

daire_f = play.new_circle(color="light blue",
    x=120,y=-200,radius=10,border_color="black",border_width=2)

text_f = play.new_text(words="Flüt",x=155,y=-200,font_size=20)

silme_sesi = pygame.mixer.Sound("clear_melody.wav")

# tuşlar ve sesleri:
kayitli_melodi = []
keys = [] # piyano tuşlarının tutulduğu liste
sounds = []
sounds.append([]) # piyano sesleri
sounds.append([]) # gitar sesleri
sounds.append([]) # violin sesleri
sounds.append([]) # flüt sesleri

for i in range(8):
    #piyano tuşları oluşturuluyor
    key_x = - 180  + i * 50  
    key = play.new_box(color='white', border_color='black', 
        border_width=3, x=key_x, y=0, width=40, height=100)

    keys.append(key)

    #piyano sesleri ekleniyor
    ses = pygame.mixer.Sound("pia"+str(i+1)+".ogg")
    sounds[0].append(ses)

    #gitar sesleri ekleniyor
    ses = pygame.mixer.Sound("git"+str(i+1)+".ogg")
    sounds[1].append(ses)

    #violin sesleri ekleniyor
    ses = pygame.mixer.Sound("vio"+str(i+1)+".ogg")
    sounds[2].append(ses)

    #flüt sesleri ekleniyor
    ses = pygame.mixer.Sound("fl"+str(i+1)+".ogg")
    sounds[3].append(ses)

@play.when_program_starts
def start():
    pygame.mixer.music.load("hi-1.mp3")
    pygame.mixer.music.play()
    
@daire_p.when_clicked
def piano_butonu():
    global enstruman
    enstruman = 0
    daire_p.color = "black"
    daire_g.color = "light blue"
    daire_v.color = "light blue"
    daire_f.color = "light blue"

@daire_g.when_clicked
def gitar_butonu():
    global enstruman
    enstruman = 1
    daire_p.color = "light blue"
    daire_g.color = "black"
    daire_v.color = "light blue"
    daire_f.color = "light blue"

@daire_v.when_clicked
def violin_butonu():
    global enstruman
    enstruman = 2
    daire_p.color = "light blue"
    daire_g.color = "light blue"
    daire_v.color = "black"
    daire_f.color = "light blue"

@daire_f.when_clicked
def flut_butonu():
    global enstruman
    enstruman = 3
    daire_p.color = "light blue"
    daire_g.color = "light blue"
    daire_v.color = "light blue"
    daire_f.color = "black"

# Ekrandaki tuşlara basılınca piyano sesi çalınacak
@play.repeat_forever
async def do():
    for i in range(len(keys)):
        if keys[i].is_clicked:
            keys[i].color = "grey"
            sounds[enstruman][i].play()
            await play.timer(seconds=0.5)
            keys[i].color = "white"
            kayitli_melodi.append(i) 

# kayotlı melodiyi çalan buton
@buton_1.when_clicked
async def muzik_cal():
    for i in range(len(kayitli_melodi)): 
        sounds[enstruman][kayitli_melodi[i]].play()
        await play.timer(seconds=0.5)

@buton_2.when_clicked
def temizle():
    kayitli_melodi.clear()
    silme_sesi.play()

play.start_program()

