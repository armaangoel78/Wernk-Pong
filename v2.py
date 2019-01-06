# This script will detect faces via your webcam.
# Tested with OpenCV3

import cv2
import time
import pygame
from loop import Loop
from controller import Controller
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from line import Line
from error import Error

pygame.init()


cap = cv2.VideoCapture(0)

cap.set(3,720/10)     #horizontal pixels
cap.set(4,480/10)     #vertical pixels
cap.set(5, 15)      #frame rate
time.sleep(2)  

# Create the haar cascade
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

run = True
up = False
down = False
	
def up():
    return up

def down():
    return down

win_w = 500
win_h = 500
win = pygame.display.set_mode((win_w, win_h))
pygame.display.set_caption("Wernk-Pong")

games = 0

while run:
    if games == 0 or (pygame.MOUSEBUTTONUP in [event.type for event in pygame.event.get()]): 
        paddle_1 = Paddle(win_w, win_h, 10, "assets/wernkepaddle3.png", 10, up, down)
        paddle_2 = Paddle(win_w, win_h, win_w - 30, "assets/beckpaddle3.png", 10, up, down)
        scoreboard = Scoreboard(win_w, win_h)
        error = Error(win_w, win_h)
        ball = Ball(paddle_1, paddle_2, scoreboard, win_w, win_h, 30, "assets/wernkeball2.png",
                    "assets/beckball.png")  # 15 seems to fast for the player
        line = Line(win_w, win_h)

        sprites = pygame.sprite.Group([paddle_1, paddle_2, scoreboard, error, ball, line])

    while run and scoreboard.player_1_score + scoreboard.player_2_score < 5:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
            #flags = cv2.CV_HAAR_SCALE_IMAGE
        )

        print("Found {0} faces!".format(len(faces)))
        if len(faces) > 0:
            error.face()
            (x, y, w, h) = faces[0]

            print(y+h/2)

            is_up = 480/4

            if (y+h/2 < 480/3):
                paddle_1.up()
                print("up")
            elif (y+h/2 > 480*2/3):
                paddle_1.down()
                print("down")
        else:
            error.noface()
        
        for (x, y, w, h) in faces:
        	cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        pygame.time.delay(5)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        win.fill((0, 0, 0))
        sprites.update()
        sprites.draw(win)
        pygame.display.update()
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    games += 1
cap.release()
cv2.destroyAllWindows()
