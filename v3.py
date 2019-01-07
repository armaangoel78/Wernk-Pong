import pygame
from loop import Loop
from controller import Controller
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from line import Line
import threading
import cv2
from error import Error

def face_stuff(paddle_1):
    win_w = 500
    win_h = 500

    cap = cv2.VideoCapture(0)

    cap.set(3, 720 / 10)  # horizontal pixels
    cap.set(4, 480 / 10)  # vertical pixels
    cap.set(5, 15)  # frame rate
    #time.sleep(2) this was in v2 for some reason it is why the game takes so long to load

    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    error = Error(win_w, win_h)

    while run and scoreboard.player_1_score + scoreboard.player_2_score < 5:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
            # flags = cv2.CV_HAAR_SCALE_IMAGE
        )

        print("Found {0} faces!".format(len(faces)))
        if len(faces) > 0:
            error.face()
            (x, y, w, h) = faces[0]

            print(y + h / 2)

            is_up = 480 / 4

            if (y + h / 2 < 480 / 3):
                paddle_1.up()
                print("up")
            elif (y + h / 2 > 480 * 2 / 3):
                paddle_1.down()
                print("down")
        else:
            error.noface()

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        #pygame.time.delay(5) I am pretty sure this is what added/caused lag

    cap.release()
    cv2.destroyAllWindows()


print('running')
pygame.init()

win_w = 500
win_h = 500
win = pygame.display.set_mode((win_w, win_h))
pygame.display.set_caption("Wernk-Pong")

controller = Controller()
paddle_1 = Paddle(win_w, win_h, 10, "assets/wernkepaddle3.png", 10, controller.w, controller.s)
paddle_2 = Paddle(win_w, win_h, win_w - 30, "assets/beckpaddle3.png", 7, controller.up, controller.down)
scoreboard = Scoreboard(win_w, win_h)
ball = Ball(paddle_1, paddle_2, scoreboard, win_w, win_h, 12, "assets/wernkeball2.png",
            "assets/beckball.png")  # 15 seems to fast for the player
line = Line(win_w, win_h)

game_sprites = pygame.sprite.Group([paddle_1, paddle_2, scoreboard, ball, line])

thread1 = threading.Thread(target=face_stuff, args=(paddle_1,))
thread1.start()

sprites = pygame.sprite.Group([paddle_1, paddle_2, scoreboard, ball, line])
run = True

while run:
    pygame.time.delay(10) #this should get us roughly to 60fps after computation

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0, 0, 0))

    controller.update()
    if (scoreboard.player_1_score + scoreboard.player_2_score < 5):
        sprites.update()
    else:
        scoreboard.update()
        print(str(scoreboard.player_1_score) + " " + str(scoreboard.player_2_score))

    sprites.draw(win)

    pygame.display.update()

pygame.quit()
print('ending the face stuff')
thread1.join()

