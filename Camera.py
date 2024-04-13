from math import pi, sin, cos
import numpy as np

class Camera:
    X_AXIS = 0
    Y_AXIS = 1
    Z_AXIS = 2

    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

        self.roll = 0
        self.pitch = 0
        self.yaw = 0

        self.pinhole_x = 400
        self.pinhole_y = 300
        self.pinhole_z = 400
        self.pinhole_z_default = 400

    def return_cords(self):
        return [self.x, self.y, self.z]

    def move_right(self, amount):
        multipliers = self.get_relative_multipliers(Camera.X_AXIS)

        self.x -= -amount * multipliers[0]
        self.y += -amount * multipliers[1]
        self.z += -amount * multipliers[2]

    def move_left(self, amount):
        multipliers = self.get_relative_multipliers(Camera.X_AXIS)

        self.x -= amount * multipliers[0]
        self.y += amount * multipliers[1]
        self.z += amount * multipliers[2]

    def move_up(self, amount):
        multipliers = self.get_relative_multipliers(Camera.Y_AXIS)

        self.x -= -amount * multipliers[0]
        self.y += -amount * multipliers[1]
        self.z -= -amount * multipliers[2]

    def move_down(self, amount):
        multipliers = self.get_relative_multipliers(Camera.Y_AXIS)

        self.x -= amount * multipliers[0]
        self.y += amount * multipliers[1]
        self.z -= amount * multipliers[2]

    def move_forward(self, amount):
        multipliers = self.get_relative_multipliers(Camera.Z_AXIS)

        self.x -= amount * multipliers[0]
        self.y -= amount * multipliers[1]
        self.z += amount * multipliers[2]

    def move_backward(self, amount):
        multipliers = self.get_relative_multipliers(Camera.Z_AXIS)

        self.x -= -amount * multipliers[0]
        self.y -= -amount * multipliers[1]
        self.z += -amount * multipliers[2]

    def rotate_roll(self, amount):
        self.roll += amount * pi / 180

    def rotate_pitch(self, amount):
        self.pitch += amount * pi / 180

    def rotate_yaw(self, amount):
        self.yaw += amount * pi / 180

    def zoom_in(self):
        self.pinhole_z *= 1.1

    def zoom_out(self):
        self.pinhole_z *= 0.9

    def reset_zoom(self):
        self.pinhole_z = self.pinhole_z_default

    def get_relative_multipliers(self, axis=0):
        yaw = np.array([
            [np.cos(self.yaw), np.sin(self.yaw), 0],
            [-np.sin(self.yaw), np.cos(self.yaw), 0],
            [0, 0, 1]
        ])

        pitch = np.array([
            [np.cos(self.pitch), 0, -np.sin(self.pitch)],
            [0, 1, 0],
            [np.sin(self.pitch), 0, np.cos(self.pitch)]
        ])

        roll = np.array([
            [1, 0, 0],
            [0, np.cos(self.roll), np.sin(self.roll)],
            [0, -np.sin(self.roll), np.cos(self.roll)]
        ])

        multipliers = np.dot(np.dot(pitch, yaw), roll)
        multipliers[:, axis][np.abs(multipliers[:, axis]) < 1e-5] = 0
        print(multipliers[:, axis])

        return multipliers[:, axis]

