import pygame
from loop import Loop
from controller import Controller
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from line import Line

print('running')
pygame.init()

win_w = 500
win_h = 500
win = pygame.display.set_mode((win_w, win_h))
pygame.display.set_caption("Wernk-Pong")

controller = Controller()
paddle_1 = Paddle(win_w, win_h, 10, "assets/wernkepaddle3.png", 10, controller.up, controller.down)
paddle_2 = Paddle(win_w, win_h, win_w - 30, "assets/beckpaddle3.png", 10, controller.up, controller.down)
scoreboard = Scoreboard(win_w, win_h)
ball = Ball(paddle_1, paddle_2, scoreboard, win_w, win_h, 30, "assets/wernkeball2.png",
            "assets/beckball.png")  # 15 seems to fast for the player
line = Line(win_w, win_h)

sprites = pygame.sprite.Group([paddle_1, paddle_2, scoreboard, ball, line])

run = True

while run:
    pygame.time.delay(5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0, 0, 0))

    controller.update()
    if (scoreboard.player_1_score + scoreboard.player_2_score < 5):
        sprites.update()
    else:
        print(str(scoreboard.player_1_score) + " " + str(scoreboard.player_2_score))
    
    sprites.draw(win)



    pygame.display.update()

# pygame.quit()
