import pygame


class Controller:
    def __init__(self):
        pygame.joystick.init()
        self.joystick = ([pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())])[0]
        self.joystick.init()

        self.update()


    def update(self):
        self.value = self.joystick.get_axis(1)

    def up(self):
        return self.value < -0.5
    
    def down(self):
        return self.value > 0.5
