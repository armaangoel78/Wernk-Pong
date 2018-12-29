import pygame


class Line(pygame.sprite.Sprite):

    def __init__(self, win_w, win_h):
        super().__init__()

        self.image = pygame.Surface([1, win_h])
        self.image.fill((255, 255, 255))
        self.rect = pygame.Rect(win_w/2, 0, 1, win_h)