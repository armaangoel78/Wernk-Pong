class Simulation_Ball:
    def __init__(self, win_w, win_h, vel, vel_x, vel_y, x, y):
        super().__init__()

        self.win_h = win_h
        self.win_w = win_w

        self.size = int(win_h / 25)
        self.height = self.size
        self.width = self.size

        self.x = x
        self.y = y

        self.vel = vel
        self.vel_x = vel_x
        self.vel_y = vel_y

    def update(self):
        self.wall_collision()

        self.x += self.vel_x
        self.y += self.vel_y

        return self.check_points()

    def wall_collision(self):
        if (self.y <= 0) or (self.y + self.height >= self.win_h):
            self.vel_y = -self.vel_y

    def check_points(self, reset=True):
        if (self.x + self.width) >= self.win_w:
            return True
        return False


def simulate_ball(vel_x, vel_y, vel, x, y):
    win_h = 500
    win_w = 500

    ball = Simulation_Ball(win_w, win_h, vel, vel_x, vel_y, x, y)

    while not ball.update():
        pass
    return ball.y
