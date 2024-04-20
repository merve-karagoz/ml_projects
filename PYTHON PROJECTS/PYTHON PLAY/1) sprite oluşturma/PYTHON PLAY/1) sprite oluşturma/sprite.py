#oyunun başlangıcı
import play

# metin şeklinde bir sprite
text = play.new_text(words = 'THE DARK KNIGHT', x = 0 , y = 0, font = None, font_size = 40)

# daire şeklinde bir sprite
cir = play.new_circle(color='green', x = -100, y = 0, radius=10)

# resim şeklinde sprite
pic = play.new_image(image='batman.png', x = 100, y =100, size=50, angle=0)


#program başladığında 1 kez gerçekleştirilen eylemler
@play.when_program_starts
def start():
    pic.hide()
    text.hide()




# program başladığında 1 kez gerçekleştirilen eylemler
@play.when_program_starts
def start():
    pass

# program çalışırken tekrarlanan eylemler
@play.repeat_forever
def do():
    pass

# yukarıdaki kodu çalıştırma sinyali
play.start_program()