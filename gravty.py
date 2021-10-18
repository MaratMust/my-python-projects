import pygame as pg
import random

pg.init()

W = 600
H = 600
g = 1
w = 20
h = 20

start = False
num = 0
maximum = 20

RE = []

disp = pg.display.set_mode((W, H))


class Rect:
    def __init__(self, x, y):
        self.y = y
        self.x = x
        self.s = 0

    def gr(self):
        self.y += self.s
        if maximum >= self.s:
            self.s += g
        if self.y + h >= H:
            self.y = H - h
            self.s *= -1

    def animetion(self):
        pg.draw.rect(disp, (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)), [self.x, self.y, w, h])


run = True


def anim():
    disp.fill((0, 0, 0))
    pg.draw.rect(disp, (255, 255, 255), [pos[0]-w//2, pos[1]-h//2, w + 1, h + 1], 1)
    for i in RE:
        i.animetion()
    pg.display.update()


while run:
    pg.time.delay(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONUP:
            pos = pg.mouse.get_pos()
            RE.append(Rect(pos[0] - w // 2, pos[1]-h//2))

    for i in RE:
        i.gr()

    pos = pg.mouse.get_pos()

    anim()

quit()
