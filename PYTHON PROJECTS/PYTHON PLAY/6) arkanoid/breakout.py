import play
from random import randint 

#EKRAN
frames = 45 #kare sayısı
lose = play.new_text(words='KAYBETTİN', font_size=100, color='red')
win = play.new_text(words='KAZANDINIZ', font_size=100, color='yellow')
#platformu oluşturalım
platform = play.new_box(color="brown",x=0,y=-270,width=150,height=20)


#topmuzu oluşturalım
top = play.new_circle(color="green",x=0,y=-150,radius=15)
tugla_liste = []

@play.when_program_starts
def start():
    lose.hide()
    win.hide()

    #  tuğlaların oluşturulması
    tugla_x = play.screen.left + 75
    tugla_y = play.screen.top - 50

    for i in range(3):
        for j in range(7):
            tugla = play.new_box(color="grey",x=tugla_x,y=tugla_y,width=110,
                height=30,border_color="dark grey",border_width=1)
            tugla_liste.append(tugla)
            tugla_x = tugla_x + tugla.width
        tugla_x = play.screen.left + 75
        tugla_y = tugla.y - tugla.height

    # kuklalara fizik özelliği verelim
    platform.start_physics(stable=True,obeys_gravity=False,x_speed=0,y_speed=0)
    top.start_physics(x_speed=35,y_speed=35,obeys_gravity=False)

@play.repeat_forever
async def game():
    #platformun hareketinı kodlayalım
    if play.key_is_pressed("right","d"):
        platform.physics.x_speed = 10
    elif play.key_is_pressed("left","a"):
        platform.physics.x_speed = -10
    else:
        platform.physics.x_speed= 0

    # Tuğlalaın yok edilmesi

    for t in tugla_liste:
        if t.is_touching(top):
            t.hide()
            tugla_liste.remove(t)
            top.physics.x_speed = -1 * top.physics.x_speed
            top.physics.y_speed = -1 * top.physics.y_speed
            top.angle= 15


    # Kazanma şartı
    if len(tugla_liste) == 0:
        win.show()
    
    # Kaybetme Şartı
    if top.y <= platform.y :
        lose.show()
        top.physics.x_speed=0
        top.physics.y_speed=0

    await play.timer(seconds=1/frames) #fotograf karelerinin değişim hızı

play.start_program()