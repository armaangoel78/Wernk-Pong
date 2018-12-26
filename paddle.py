import pygame


class Paddle(pygame.sprite.Sprite):

    def __init__(self, win_w, win_h, x, image_path, vel, up_command, down_command):
        super().__init__()

        self.win_h = win_h

        width, height = int(win_w/50), int(win_h/5)

        y = win_h/2 - height/2

        self.rect = pygame.Rect(x, y, width, height)
        self.vel = vel

        self.image = pygame.transform.scale(pygame.image.load(image_path), (width, height))

        self.up_command = up_command
        self.down_command = down_command

    def update(self, *args):
        if self.up_command():
            self.up()

        if self.down_command():
            self.down()

    def up(self):
        self.rect.y -= self.vel
        if self.rect.y < 0:
            self.rect.y = 0

    def down(self):
        self.rect.y += self.vel
        if self.rect.y + self.rect.height > self.win_h:
            self.rect.y = self.win_h - self.rect.height
