import pygame

class Error(pygame.sprite.Sprite):

    def __init__(self, win_w, win_h):
        super().__init__()

        self.text = ""
        self.win_w = win_w
        self.win_h = win_h

        self.font = pygame.font.SysFont("Arial", 20)
        self.image = pygame.Surface((self.win_w/5, self.win_h/10))
        self.rect = pygame.Rect(self.win_w/2 - self.image.get_width()/2, 50, self.image.get_width(), self.image.get_height())

    def noface(self):
        self.text = "No Face"

    def face(self):
        self.text = ""

    def update(self, *args):
        textSurf = self.font.render(self.text, 1, (255, 255, 255))
        self.image = pygame.Surface((self.win_w/5, self.win_h/5))
        W = textSurf.get_width()
        H = textSurf.get_height()
        self.image.blit(textSurf, [self.rect.w / 2 - W / 2, self.rect.h / 2 - H / 2])
