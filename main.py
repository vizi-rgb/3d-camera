import pygame as pg
from WindowConfig import WindowConfig

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
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_DOWN:
                    print("Arrow down")
                elif event.key == pg.K_UP:
                    print("Arrow up")
                elif event.key == pg.K_LEFT:
                    print("Arrow left")
                elif event.key == pg.K_RIGHT:
                    print("Arrow right")
        clock.tick(fps)
    pg.quit()

if __name__ == '__main__':
    main()
