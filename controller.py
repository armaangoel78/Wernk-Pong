import pygame


class Controller:
    def __init__(self):
        self.keys = None

    def update(self):
        self.keys = pygame.key.get_pressed()

    def w(self):
        return self.keys[pygame.K_w]
    
    def s(self):
        return self.keys[pygame.K_s]

    def up(self):
        return self.keys[pygame.K_UP]
    
    def down(self):
        return self.keys[pygame.K_DOWN]


   