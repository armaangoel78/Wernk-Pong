import pygame


class Scoreboard(pygame.sprite.Sprite):

    def __init__(self, win_w, win_h):
        super().__init__()

        self.player_1_score = 0
        self.player_2_score = 0

        self.win_h = win_h
        self.win_w = win_w

        self.font = pygame.font.SysFont("Arial", 20)
        self.image = pygame.Surface((self.win_w/5, self.win_h/10))
        self.rect = pygame.Rect(self.win_w/2 - self.image.get_width()/2, 0, self.image.get_width(), self.image.get_height())

    def player_1_point(self):
        self.player_1_score += 1

    def player_2_point(self):
        self.player_2_score += 1

    def update(self, *args):
        score = str(self.player_1_score)+ " " + str(self.player_2_score)
        print(score)

        textSurf = self.font.render(score, 1, (255, 255, 255))
        self.image = pygame.Surface((self.win_w/5, self.win_h/5))
        W = textSurf.get_width()
        H = textSurf.get_height()
        self.image.blit(textSurf, [self.rect.w / 2 - W / 2, self.rect.h / 2 - H / 2])
