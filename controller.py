import pygame


class Controller:
    def __init__(self):
        pygame.joystick.init()
        joysticks = ([pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())])
        if len(joysticks) > 0:
            self.joystick = joysticks[0]
            self.joystick.init()
        else: 
            self.joystick = None

        self.update()


    def update(self):
        if self.joystick != None:
            self.value = self.joystick.get_axis(1)

    def up(self):
        return self.value < -0.5
    
    def down(self):
        return self.value > 0.5
