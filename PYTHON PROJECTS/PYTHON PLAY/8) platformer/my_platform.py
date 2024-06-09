import play
import pygame
from random import randint

play.set_backdrop('light green')
pygame.display.set_caption("Platformer Oyunu")

#Sesleri eklemelisin
deniz_sesi = pygame.mixer.Sound("sea.ogg")
altin_sesi = pygame.mixer.Sound("coin.wav")
pygame.mixer_music.load("soundtrack.mp3")

#oyuncu ekleniyor
oyuncu = play.new_circle(color="white",x=-370,y=230,radius=15,border_color="black",border_width=2)

#Skor Sayacı
score_txt = play.new_text(words='Score:', x=play.screen.right-100, y=play.screen.top-30, size=70)
score = play.new_text(words='0', x=play.screen.right-30, y=play.screen.top-30, size=70)

#ipucu
text = play.new_text(words='Tap SPACE to jump, LEFT/RIGHT to move', x=0, y=play.screen.bottom+60, size=70)

sea = play.new_box(
        color='blue', width=play.screen.width, height=50, x=0, y=play.screen.bottom+20
    )

altin_listesi = []

def draw_platforms():
    #platformları oluşturcaz
    platform1 = play.new_box(color="brown",x=-320,y=130,width=150,height=30,border_width=2,border_color="black")
    platform1.start_physics(can_move=False,stable=True,obeys_gravity=False)

    platform2 = play.new_box(color="brown",x=-70,y=130,width=250,height=30,border_width=2,border_color="black")
    platform2.start_physics(can_move=False,stable=True,obeys_gravity=False)

    platform3 = play.new_box(color="brown",x=150,y=180,width=100,height=30,border_width=2,border_color="black")
    platform3.start_physics(can_move=False,stable=True,obeys_gravity=False)

    platform4 = play.new_box(color="brown",x=270,y=130,width=130,height=30,border_width=2,border_color="black")
    platform4.start_physics(can_move=False,stable=True,obeys_gravity=False)

def draw_coins(): 
    #altınları oluşturcaz
    altin1 = play.new_circle(color="yellow",x=-70,y=170,radius=10)
    altin2 = play.new_circle(color="yellow",x=300,y=170,radius=10)
    altin_listesi.append(altin1)
    altin_listesi.append(altin2)

@play.when_program_starts
def start():
    #fon müziği eklenecek ve çalınacak
    pygame.mixer_music.play()

    # kuklanın fizik özelliğini açalım
    oyuncu.start_physics(can_move=True,stable=False,obeys_gravity=True,bounciness=0.5)
    draw_platforms()
    draw_coins()

@play.repeat_forever
async def game():

    # altın toplama suya düşme ve oyuncunun hareketi kodlanacak
    print(oyuncu.x)
    if play.key_is_pressed("right"):      
        oyuncu.physics.x_speed = 10
    
    elif play.key_is_pressed("left"):
        oyuncu.physics.x_speed = -10
    elif play.key_is_pressed("space"):
        oyuncu.physics.y_speed = 50
        await play.timer(seconds=1)
        oyuncu.physics.y_speed = 0
    else:
        oyuncu.physics.x_speed = 0


    # denize düşme
    if oyuncu.is_touching(sea):
        deniz_sesi.play()
        oyuncu.hide()
        await play.timer(seconds=1000) 
        quit()

    # altın toplama
    for i in altin_listesi:
        if i.is_touching(oyuncu):
            altin_sesi.play()
            altin_listesi.remove(i)
            i.hide()
            score.words = int(score.words) + 1

    await play.timer(seconds=1/48)

play.start_program()