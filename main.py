import pygame as pg
from WindowConfig import WindowConfig
from Wireframe import Wireframe
from Camera import Camera
from Renderer import Renderer

def config():
    wc = WindowConfig()
    pg.display.set_mode((wc.get_width(), wc.get_height()))
    pg.display.set_caption(wc.get_title())


def main():
    pg.init()
    config()
    clock = pg.time.Clock()

    running = True
    fps = 60
    wireframe = Wireframe.from_file("initial_obj.txt")
    camera = Camera()
    renderer = Renderer([wireframe], camera)
    amount = 10

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    camera.move_left(amount)
                if event.key == pg.K_RIGHT:
                    camera.move_right(amount)
                if event.key == pg.K_UP:
                    camera.move_forward(amount)
                if event.key == pg.K_DOWN:
                    camera.move_backward(amount)
                if event.key == pg.K_LSHIFT:
                    camera.move_up(amount)
                if event.key == pg.K_LCTRL:
                    camera.move_down(amount)
                if event.key == pg.K_w:
                    camera.rotate_roll(amount)
                if event.key == pg.K_s:
                    camera.rotate_roll(-amount)
                if event.key == pg.K_q:
                    camera.rotate_pitch(amount)
                if event.key == pg.K_e:
                    camera.rotate_pitch(-amount)
                if event.key == pg.K_a:
                    camera.rotate_yaw(amount)
                if event.key == pg.K_d:
                    camera.rotate_yaw(-amount)
                if event.key == pg.K_EQUALS:
                    pass
                if event.key == pg.K_MINUS:
                    pass


        pg.display.get_surface().fill((0, 0, 0))
        renderer.render()
        pg.display.flip()
        clock.tick(fps)

    pg.quit()


if __name__ == '__main__':
    main()
