import pygame

from controller import Controller
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

pygame.init()

win_w = 500
win_h = 500
win = pygame.display.set_mode((win_w, win_h))
pygame.display.set_caption("Wernk-Pong")

controller = Controller()

paddle_1 = Paddle(win_w, win_h, 10, "assets/wernkepaddle3.png", 10, controller.w, controller.s)
paddle_2 = Paddle(win_w, win_h, win_w - 30, "assets/beckpaddle3.png", 10, controller.up, controller.down)
scoreboard = Scoreboard(win_w, win_h)
ball = Ball(paddle_1, paddle_2, scoreboard, win_w, win_h, 10, "assets/wernkeball2.png", "assets/beckball.png")

sprites = pygame.sprite.Group([paddle_1, paddle_2, scoreboard, ball])

run = True
while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0,0,0))

    controller.update()

    sprites.update()
    sprites.draw(win)

    pygame.display.update()

pygame.quit()