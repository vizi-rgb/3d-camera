from math import pi

class Camera:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.roll = 0
        self.pitch = 0
        self.yaw = 0
        self.pinhole_x = 0
        self.pinhole_y = 0
        self.pinhole_z = 400

    def return_cords(self):
        return [self.x, self.y, self.z]

    def move_right(self, amount):
        self.x += amount

    def move_left(self, amount):
        self.x -= amount

    def move_up(self, amount):
        self.y += amount

    def move_down(self, amount):
        self.y -= amount

    def move_forward(self, amount):
        self.z += amount

    def move_backward(self, amount):
        self.z -= amount

    def rotate_roll(self, amount):
        self.roll += amount * pi / 180

    def rotate_pitch(self, amount):
        self.pitch += amount * pi / 180

    def rotate_yaw(self, amount):
        self.yaw += amount * pi / 180

