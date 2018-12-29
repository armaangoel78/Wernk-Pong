import pygame


class Text(pygame.sprite.Sprite):

    def __init__(self, x, y, size, text):
        super().__init__()

        self.font = pygame.font.SysFont("Arial", size)
        self.textSurf = self.font.render(text, 1, (255, 255, 255))
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        self.image = pygame.Surface((W, H))
        self.image.blit(self.textSurf, [0,0])
        self.rect = pygame.Rect(x, y, W, H)
