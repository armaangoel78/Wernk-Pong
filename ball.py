import random, math
from paddle import Paddle

class Ball:
    def __init__(self, paddle1, paddle2, win_h, win_w, size, speed, color):
        self.paddle1 = paddle1
        self.paddle2 = paddle2 
        self.win_h = win_h
        self.win_w = win_w
        self.size = size
        self.speed = speed
        self.color = color
        self.restart()

    def restart(self):
        self.x = self.win_w/2 - self.size/2
        self.y = self.win_h/2 - self.size/2
        angle = random.randint(0,360)
        self.vel_x = self.speed * math.cos(angle)
        self.vel_y = self.speed * math.sin(angle)

    def update(self):
        if (self.wall_collision()):
            self.vel_y = -self.vel_y

        if (self.paddle1_collision() or self.paddle2_collision()):
            self.vel_x = -self.vel_x

        self.x += self.vel_x
        self.y += self.vel_y

        if (self.left()):
            self.restart()

    def wall_collision(self):
        return (self.y <= 0) or (self.y+self.size >= self.win_h)

    def paddle1_collision(self):
        return (self.vel_x < 0) and (self.x <= self.paddle1.x + self.paddle1.width) and (self.y <= self.paddle1.y + self.paddle1.height) and (self.y + self.size >= self.paddle1.y)

    def paddle2_collision(self):
        return  (self.vel_x > 0) and (self.x + self.size >= self.paddle2.x) and (self.y <= self.paddle2.y + self.paddle2.height) and (self.y + self.size >= self.paddle2.y)

    def left(self):
        return (self.x <= 0) or (self.x + self.size >= self.win_w)

    def cords(self):
        return (self.x, self.y, self.size, self.size)