import numpy as np
from Camera import Camera
from Wireframe import Wireframe
import pygame as pg


class Renderer:
    def __init__(self, scene: list[Wireframe], camera: Camera, windowconfig):
        self.scene = scene
        self.camera = camera
        self.wc = windowconfig

    def interpolate(self, v0, v1, t):
        return v0 + t * (v1 - v0)

    def clip_edge(self, v0, v1, z_clip):
        t = (0 - v0[2]) / (v1[2] - v0[2])
        x = self.interpolate(v0[0], v1[0], t)
        y = self.interpolate(v0[1], v1[1], t)
        return np.array([x, y, z_clip])


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

                if d_start[2] < 0.1 and d_end[2] < 0.1:
                    continue

                if d_start[2] < 0.1:
                    d_start = self.clip_edge(d_start, d_end, 0.1)
                elif d_end[2] < 0.1:
                    d_end = self.clip_edge(d_start, d_end, 0.1)


                bx1 = float(self.camera.pinhole_z / d_start[2] * d_start[0] + self.camera.pinhole_x)
                by1 = float(self.camera.pinhole_z / d_start[2] * d_start[1] + self.camera.pinhole_y)

                bx2 = float(self.camera.pinhole_z / d_end[2] * d_end[0] + self.camera.pinhole_x)
                by2 = float(self.camera.pinhole_z / d_end[2] * d_end[1] + self.camera.pinhole_y)

                # print(f"2D: {bx1} {by1} {bx2} {by2}")

                pg.draw.line(pg.display.get_surface(), wireframe.get_color(), (bx1, by1), (bx2, by2))


