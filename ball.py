import random, math
import pygame


class Ball(pygame.sprite.Sprite):

    def __init__(self, paddle_1, paddle_2, scoreboard, win_w, win_h, vel):
        super().__init__()

        self.paddle_1 = paddle_1
        self.paddle_2 = paddle_2
        self.scoreboard = scoreboard

        self.win_h = win_h
        self.win_w = win_w

        self.image = pygame.Surface([win_h/50, win_h/50])
        self.image.fill((255, 255, 255))
        self.rect = pygame.Rect(0, 0, win_h/50, win_h/50)

        self.vel = vel
        self.vel_x = None
        self.vel_y = None

        self.restart()

    def restart(self):
        self.rect.x = self.win_w/2 - self.rect.height/2
        self.rect.y = self.win_h/2 - self.rect.width/2

        angle = random.randint(0,360)
        self.vel_x = self.vel * math.cos(angle)
        self.vel_y = self.vel * math.sin(angle)

    def update(self):
        if self.wall_collision():
            self.vel_y = -self.vel_y

        if self.paddle_1_collision() or self.paddle_2_collision():
            self.vel_x = -self.vel_x

        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        if self.left_screen():
            if self.player_1_point():
                self.scoreboard.player_1_point()
            else:
                self.scoreboard.player_2_point()
            self.restart()

    def wall_collision(self):
        return (self.rect.y <= 0) or (self.rect.y + self.rect.height >= self.win_h)

    def paddle_1_collision(self):
        return self.vel_x < 0 and pygame.sprite.spritecollide(self, [self.paddle_1], False)

    def paddle_2_collision(self):
        return self.vel_x > 0 and pygame.sprite.spritecollide(self, [self.paddle_2], False)

    def left_screen(self):
        return (self.rect.x <= 0) or (self.rect.x + self.rect.width >= self.win_w)

    def player_1_point(self):
        return self.rect.x <= 0

    def player_2_point(self):
        return self.rect.x + self.rect.width >= self.win_w