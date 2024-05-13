#oyun başlangıcı
import play
from random import randint

w = play.screen.width
h = play.screen.height

#programın dış arayüzü için nesnelerin oluşturulması
place1 = play.new_box(color = 'light green', x = 0, y = 0, width = 100, height = 200, border_width=5, border_color='green')

place2 = play.new_box(color = 'light green', x = 0, y = 0, width = 100, height = 200, border_width=5, border_color='green')

place3 = play.new_box(color = 'light green', x = 0, y = 0, width = 100, height = 200, border_width=5, border_color='green')

hello = play.new_text(words = 'Selam, tuşa basarak şansını dene!', x = 0, y = 0, font = None, font_size=40, color = 'green')

result = play.new_text(words = 'Kazandın!', x = 0, y = 0, font = None, font_size=40, color = 'green')

button = play.new_box(color = 'yellow', x = 0, y = 0, width = 150, height = 50)

button_text = play.new_text(words= 'Başla!', x = 0, y = 0, font = None, font_size = 50)

count = play.new_text(words = '0', x = 200, y = -200, font = None, font_size = 30)

count_text = play.new_text (words = 'Başarısız deneme sayısı:', x = 0, y = -200, font = None, font_size = 30)

money = play.new_text(words = '50', x = 80, y = -150, font = None, color = 'yellow', font_size = 30)

money_text = play.new_text (words = 'Kalan jeton:', x = 0, y = -150, font = None, color = 'yellow', font_size = 30)

#rastgele sayıların oluşturulması 
num1_text = play.new_text(words = '', x = -200, y = 0, font = None, font_size = 100)

num2_text = play.new_text(words = '', x = 0, y = 0, font = None, font_size = 100)

num3_text = play.new_text(words = '', x = 200, y = 0, font = None, font_size = 100)

@play.when_program_starts
def start():
    place1.x = -200
    place2.x = 0
    place3.x = 200
    hello.y = 250
    result.y = -250
    button.y = 170
    button_text.y = 170

    num1_text.hide()
    num2_text.hide()
    num3_text.hide()
    result.hide()

@play.repeat_forever
def do():
    pass

@button.when_clicked
async def clicking():
    num1 = randint(0, 10)
    num2 = randint(0, 10)
    num3 = randint(0, 10)

    num1_text.words = str(num1)
    num2_text.words = str(num2)
    num3_text.words = str(num3)

    num1_text.show()
    num2_text.show()
    num3_text.show()

    c = int(count.words)
    n = int(money.words)
    
    if num1 == num2 and num2 == num3 and num3 == num1:
        result.words = 'Kazandın!'
        c = 0
        n = n + 100
    else:
        result.words = 'Kaybettin! Ama tekrar deneyebilirsin.'
        c = c+1
        n = n - 5

    count.words = c
    money.words = n
    result.show()
    await play.timer(seconds=2.0)
    num1_text.hide()
    num2_text.hide()
    num3_text.hide()
    result.hide()


play.start_program()




