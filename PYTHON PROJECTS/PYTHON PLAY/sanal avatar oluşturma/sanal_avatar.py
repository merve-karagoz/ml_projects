'''cmd pip install pygame
pip install replit_play

py -3 -m pip install pygame
py -3 -m pip install replit_play

'''

import pygame
import play
from pygame.locals import *

#sprite (varsayılan olarak gülümsüyor)
player = play.new_image(image='wizarding-world-portrait.png', x=0, y=0, size = 100)
speech = play.new_text(words=None, x = 0, y = -play.screen.height/2 + 20)

@play.when_program_starts
def start():
    tutorial = play.new_text(words = 's - sevmek, b - beslemek, t - temizlemek, o - oyun oynamak, boşluk - çıkış', x = 0, y = 0, font_size = 20)
    tutorial.y = play.screen.height/2 - 30
    speech.words = 'Selam, arkadaş olalım mı? '

@play.repeat_forever
async def do ():
    if play.key_is_pressed('s') or play.key_is_pressed('S'):
        player.image = 'wizarding-world-portrait.png'
        speech.words = 'Mmm... Çok güzel'
        await play.timer(seconds = 2.0)
        player.image = 'wizarding-world-portrait.png'
        speech.words = 'Bu kadar mı? Biraz daha sevebilir misin?..'

    #beslenmeye rastgele bir tepki
    if play.key_is_pressed('b') or play.key_is_pressed('B'):
        player.image = 'wizarding-world-portrait.png'
        speech.words = 'Oh, çok lezzetli!'
        await play.timer(seconds = 2.0)
        player.image = 'wizarding-world-portrait.png'
        speech.words = 'Sanırım temizlenmem lazım'

    #evcil hayvanın temizlenmesi
    if play.key_is_pressed('t') or play.key_is_pressed('T'):
        player.image = 'wizarding-world-portrait.png'
        speech.words = 'Yaşasın! Mis gibi oldum!'
        await play.timer(seconds = 2.0)
        player.image = 'wizarding-world-portrait.png'
        speech.words = 'Şimdi ne yapalım?'

    #oyun zamanı
    if play.key_is_pressed('o') or play.key_is_pressed('O'):
        player.image = 'wizarding-world-portrait.png'
        speech.words = 'Ahaha, çok eğlenceli birisin!'
        await play.timer(seconds = 2.0)
        player.image = 'wizarding-world-portrait.png'
        speech.words = 'Of, sanırım yorulmuşum'
        
    #oyun sonu
    if play.key_is_pressed('space'):
        player.image = 'wizarding-world-portrait.png'
        speech.words = 'Gidiyor musun? Seni özlerim!'
        await play.timer(seconds = 2.0)

play.start_program()

