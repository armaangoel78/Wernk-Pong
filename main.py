import pygame
from paddle import Paddle
from ball import Ball

pygame.init()

win_w = 500
win_h = 500
win = pygame.display.set_mode((win_w, win_h))
pygame.display.set_caption("Wernk-Pong")

paddle1 = Paddle(win_h, 50, 10, 10, 10, (255, 255, 255))
paddle2 = Paddle(win_h, 50, 10, win_w-20, 10, (255, 255, 255))
ball = Ball(paddle1, paddle2, win_h, win_w, 20, 10, (255, 255, 255))

run = True
while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        paddle1.up()

    if keys[pygame.K_s]:
        paddle1.down()

    if keys[pygame.K_UP]:
        paddle2.up()

    if keys[pygame.K_DOWN]:
        paddle2.down()

    ball.update()

    win.fill((0,0,0))
    pygame.draw.rect(win, paddle1.color, paddle1.cords())
    pygame.draw.rect(win, paddle2.color, paddle2.cords())
    pygame.draw.rect(win, ball.color, ball.cords())
    pygame.display.update()

pygame.quit()