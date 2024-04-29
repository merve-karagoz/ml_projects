# programın başlangıcı

import play
import pygame
frames = 48
step = 10

# sprite tanımlama
player = play.new_circle(color='green', x = 0, y = -270, radius = 20, border_color='light green')

# engellerin tanımaması
wall1 = play.new_box(color='black', x = 0, y = 0, widht = 100, height = 10)
wall2 = play.new_box(color = 'black', x = -50, y = 10, width = 10,height = 100)
wall3 = play.new_box(color = 'black', x = 50, y = -10, width = 10,height = 100)
wall4 = play.new_box(color = 'black', x = 100, y = -110, width = 10,height = 100)
wall5 = play.new_box(color = 'black', x = 145, y = -160, width = 100,height = 10)
wall6 = play.new_box(color = 'black', x = -145, y = -150, width = 100,height = 10)
wall7 = play.new_box(color = 'black', x = -175, y = -200, width = 300,height = 10)
wall8 = play.new_box(color = 'black', x = -195, y = -50, width = 10,height = 300)
wall9 = play.new_box(color = 'black', x = -300, y = 10, width = 200,height = 10)
wall10 = play.new_box(color = 'black', x = -300, y = -40, width = 10,height = 100)
wall11 = play.new_box(color = 'black', x = -290, y = 100, width = 200,height = 10)
wall12 = play.new_box(color = 'black', x = 290, y = 100, width = 200,height = 10)
wall13 = play.new_box(color = 'black', x = 100, y = 50, width = 10,height = 300)
wall14 = play.new_box(color = 'black', x = 0, y = 100, width = 150,height = 10)
wall15 = play.new_box(color = 'black', x = -130, y = 100, width = 10,height = 300)

# biitiş noktası
finish = play.new_text(words='finish', x=0, y=270, font=None, font_size=50)

@play.when_program_starts
def start():
    player.start_physics(bounciness=0.2)
    wall1.start_physics(can_move=False)
    wall2.start_physics(can_move=False)
    wall3.start_physics(can_move=False)
    wall4.start_physics(can_move=False)
    wall5.start_physics(can_move=False)
    wall6.start_physics(can_move=False)
    wall7.start_physics(can_move=False)
    wall8.start_physics(can_move=False)
    wall9.start_physics(can_move=False)
    wall10.start_physics(can_move=False)
    wall11.start_physics(can_move=False)
    wall12.start_physics(can_move=False)
    wall13.start_physics(can_move=False)
    wall14.start_physics(can_move=False)
    wall15.start_physics(can_move=False)

# sprite'nin hareketlerni belirlenmesi
@play.repeat_forever

async def game():
    player.physics.x_speed = 0
    player.physics.y_speed = 0

    if play.key_is_pressed('w', 'up'):
        player.physics.y_speed = step
    if play.key_is_pressed('s', 'down'):
        player.physics.y_speed = -1 * step
    if play.key_is_pressed('a', 'left'):
        player.physics.x_speed = -1 * step
    if play.key_is_pressed('d', 'right'):
        player.physics.x_speed = step

    if player.is_touching(finish):
        wall1.hide()
        wall2.hide()
        wall3.hide()
        wall4.hide()
        wall5.hide()
        wall6.hide()
        wall7.hide()
        wall8.hide()
        wall9.hide()
        wall10.hide()
        wall11.hide()
        wall12.hide()
        wall13.hide()
        wall14.hide()
        wall15.hide()
        finish.hide()
        play.new_text(words='YOU WIN!', x = 0, y = 0, font=None, font_size= 100, color='yellow')

    await play.timer(seconds=1/frames)
#programın sonu (başlangıcı)
play.start_program()