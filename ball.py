import random
import numpy as np
import pygame
from ai_support import simulate_ball
import math
from keras.models import load_model
from time import sleep


# 500 is the bottom for y
def play_ai(ball, paddle):
    model = ball.model

    vel_x = (ball.vel_x) / ball.actual_vel
    vel_y = ball.vel_y / ball.actual_vel
    x = (ball.rect.x) / 500
    y = ball.rect.y / 500
    destination = model.predict(np.array([[vel_x, vel_y, x, y]])) * 500

    if destination > paddle.rect.y + paddle.rect.height / 2:
        #print(paddle.rect.y, destination, (ball.vel_x, ball.vel_y, ball.vel, ball.rect.x, ball.rect.y),
              #simulate_ball(ball.vel_x, ball.vel_y, ball.vel, ball.rect.x, ball.rect.y) if ball.vel_x >= 0 else -1, 'd')
        paddle.down()
    else:
        #print(paddle.rect.y, destination, (ball.vel_x, ball.vel_y, ball.vel, ball.rect.x, ball.rect.y),
              #simulate_ball(ball.vel_x, ball.vel_y, ball.vel, ball.rect.x, ball.rect.y) if ball.vel_x >= 0 else -1, 'u')
        paddle.up()


class Ball(pygame.sprite.Sprite):

    def __init__(self, paddle_1, paddle_2, scoreboard, win_w, win_h, vel, player_1_hit_image_path,
                 player_2_hit_image_path):
        super().__init__()

        self.paddle_1 = paddle_1
        self.paddle_2 = paddle_2
        self.scoreboard = scoreboard

        self.win_h = win_h
        self.win_w = win_w

        self.size = int(win_h / 25)

        self.image = pygame.Surface([self.size, self.size])
        self.image.fill((255, 255, 255))
        self.rect = pygame.Rect(0, 0, self.size, self.size)

        self.vel = vel
        self.vel_x = None
        self.vel_y = None

        self.player_1_hit_image_path = player_1_hit_image_path
        self.player_2_hit_image_path = player_2_hit_image_path

        self.frame_count = 0
        self.model = load_model('pong_ai_2.h5')

        self.actual_vel = vel

        self.restart()

    def set_image(self, image_path):
        self.image = pygame.transform.scale(pygame.image.load(image_path), (self.size, self.size))

    def restart(self):
        self.rect.x = self.win_w / 2 - self.rect.height / 2
        self.rect.y = self.win_h / 2 - self.rect.width / 2

        self.paddle_1.rect.y = self.win_h / 2 - self.paddle_1.rect.height / 2
        self.paddle_2.rect.y = self.win_h / 2 - self.paddle_2.rect.height / 2

        angle = random.uniform(-60, 60)  # [random.randint(0,1) * 180 + random.randint(-60,60) for x in range(10)]
        self.change_direction(angle)

        sleep(.75)

    def change_direction(self, angle):
        angle = angle / 180 * math.pi
        self.vel_x = math.floor(self.vel * math.cos(angle))
        self.vel_y = math.floor(self.vel * math.sin(angle))
        self.actual_vel = (self.vel_x ** 2 + self.vel_y ** 2) ** .5

    def update(self):
        self.check_collisions()

        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # if self.frame_count is 10:
        play_ai(self, self.paddle_2)

        self.check_points()

        self.image = pygame.transform.rotate(self.image, 90)

    # Collisions

    def check_collisions(self):
        self.wall_collision()
        self.paddle_1_collision()
        self.paddle_2_collision()

    def wall_collision(self):
        if (self.rect.y <= 0) or (self.rect.y + self.rect.height >= self.win_h):
            self.vel_y = -self.vel_y

    def paddle_1_collision(self):
        if self.vel_x < 0 and pygame.sprite.spritecollide(self, [self.paddle_1], False):
            self.set_image(self.player_1_hit_image_path)

            percent_offset = ((self.rect.y + self.rect.height / 2) - (
                    self.paddle_1.rect.y + self.paddle_1.rect.height / 2)) / self.paddle_1.rect.height
            angle = 60 * percent_offset * np.random.choice([-1, 1], 1)[0]
            self.change_direction(angle)

    def paddle_2_collision(self):
        if self.vel_x > 0 and pygame.sprite.spritecollide(self, [self.paddle_2], False):
            self.set_image(self.player_2_hit_image_path)

            percent_offset = ((self.rect.y + self.rect.height / 2) - (
                    self.paddle_2.rect.y + self.paddle_2.rect.height / 2)) / self.paddle_2.rect.height
            angle = 180 + 60 * percent_offset * np.random.choice([-1, 1], 1)[0]
            self.change_direction(angle)

    # Points

    def check_points(self):
        player_2_point = self.rect.x <= 0
        player_1_point = self.rect.x + self.rect.width >= self.win_w

        if player_1_point or player_2_point:
            if player_1_point:
                self.scoreboard.player_1_point()
            else:
                self.scoreboard.player_2_point()

            self.restart()

            return True

        return False
