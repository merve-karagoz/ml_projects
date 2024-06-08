import play
import time
import pygame
from random import randint

pygame.mixer_music.load('hello.mp3')
pygame.mixer_music.play()
play.set_backdrop('light green')
hello_txt=play.new_text(words='10 tane yumurta yakala!', x=0, y=play.screen.height/2-30)

eggs_amount=play.new_text(words='0', x=300, y=play.screen.height/2-30, color='yellow')

backet=play.new_image(image='sepet.png', x=0, y=-play.screen.height/2+50, size=20)
#backet=play.new_image(image='archi.png', x=0, y=-play.screen.height/2+80, size=80)
frames = 48 
old_time = 0 # yumurtanın gözüktüğü zaman

#ilk yumurta oluşturuluyor
yumurta = play.new_circle(color="white",x=0,y=0,radius=30,border_color="black",border_width=2)
yumurta_listesi = [yumurta]
#yumurta_listesi.append(yumurta)


@play.when_program_starts
def start():
    global old_time
    old_time = time.time()
    backet.start_physics(
        stable=True, obeys_gravity=False, bounciness=1, mass=10
    )
    #ilk yumurtanın konumu ayarlanıyor
    #yumurta.x = randint(-380,380)
    yumurta_listesi[0].x = randint(-380,380)
    yumurta_listesi[0].y = 230


@play.repeat_forever
async def game():
    global old_time
    #sepetin hareket ettirilmesi
    if play.key_is_pressed("right"):
        if backet.physics.x_speed < 60:  # Max hızı 60 olarak belirleyebilirsiniz
            backet.physics.x_speed += 2  # veya istediğiniz bir artış miktarını seçebilirsiniz
    elif play.key_is_pressed("left"):
        if backet.physics.x_speed < 60:  # Max hızı 60 olarak belirleyebilirsiniz
            backet.physics.x_speed -= 2 
    else:
        backet.physics.x_speed = 0
    #yumurtanın yakalanması

    for i in yumurta_listesi :
        if i.is_touching(backet):
            yumurta_listesi.remove(i)
            i.hide()
            eggs_amount.words = int(eggs_amount.words) + 1
        i.y = i.y - 3 # yumurtanın aşağı süzülmesi

            # kaybetme kontrolü
        if i.y < backet.y :
            lose = play.new_text(words="KAYBETTİNİZ...",x=0,y=0,color="RED",font_size=100)
            backet.hide()
            await play.timer(seconds=3)
            quit() # beyaz oyun penceresini kapatır

    # diğer yumurtaların oluşturulması
    
    if time.time() - old_time > 3:
        yeni_yumurta = play.new_circle(color="white",x=0,y=0,radius=30,border_color="black",border_width=2)
        yeni_yumurta.x = randint(-380,380)
        yeni_yumurta.y = 230
        yumurta_listesi.append(yeni_yumurta)
        
        old_time = time.time()


    # kazanma kontrolü
    if int(eggs_amount.words) == 10 :
        win = play.new_text(words="KAZANDINIZ...",x=0,y=0,color="green",font_size=100)
        backet.hide()
        await play.timer(seconds=3)
        quit() # beyaz oyun penceresini kapatır
    

play.start_program()