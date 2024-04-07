import numpy as np
from Camera import Camera
from Wireframe import Wireframe
import pygame as pg

class Renderer:
    def __init__(self, scene: list[Wireframe], camera: Camera):
        self.scene = scene
        self.camera = camera


    def calculate_view_matrix(self, point):
        roll = np.array([
            [1, 0, 0],
            [0, np.cos(self.camera.roll), np.sin(self.camera.roll)],
            [0, -np.sin(self.camera.roll), np.cos(self.camera.roll)]
        ])

        pitch = np.array([
            [np.cos(self.camera.pitch), 0, -np.sin(self.camera.pitch)],
            [0, 1, 0],
            [np.sin(self.camera.pitch), 0, np.cos(self.camera.pitch)]
        ])

        yaw = np.array([
            [np.cos(self.camera.yaw), np.sin(self.camera.yaw), 0],
            [-np.sin(self.camera.yaw), np.cos(self.camera.yaw), 0],
            [0, 0, 1]
        ])

        return roll @ pitch @ yaw @ (point - self.camera.return_cords())

    def render(self):
        for wireframe in self.scene:
            for line in wireframe.lines:
                d_start = self.calculate_view_matrix(np.array([line.start.x, line.start.y, line.start.z]))
                d_end = self.calculate_view_matrix(np.array([line.end.x, line.end.y, line.end.z]))
                bx1 = float(400 / d_start[2] * d_start[0] + 0)
                by1 = float(400 / d_start[2] * d_start[1] + 0)

                bx2 = float(400 / d_end[2] * d_end[0] + 0)
                by2 = float(400 / d_end[2] * d_end[1] + 0)

                pg.draw.line(pg.display.get_surface(), (255, 255, 255), (bx1, by1), (bx2, by2))


