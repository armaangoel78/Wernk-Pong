class Paddle:
    def __init__(self, win_h, height, width, x, vel, color):
        self.win_h = win_h
        self.height = height
        self.width = width
        self.x = x
        self.y = win_h/2 - height/2
        self.vel = vel
        self.color = color

    
    def up(self):
        self.y -= self.vel
        if (self.y < 0):
            self.y = 0

    def down(self):
        self.y += self.vel
        if (self.y + self.height > self.win_h):
            self.y = self.win_h - self.height

    def cords(self):
        return (self.x, self.y, self.width, self.height)