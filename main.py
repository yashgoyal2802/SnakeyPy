import pygame
from tkinter import *
import math
import random


class cube(object):
    rows = 20
    w = 500

    def __init__(self, start, dirx=1, diry=0, color=(255, 0, 0)):
        self.pos = start
        self.dirx = 1
        self.diry = 0
        self.color = color

    def move(self, dirx, diry):
        self.dirx = dirx
        self.diry = diry
        self.pos = (self.pos[0] + self.dirx, self.pos[1] + self.diry)

    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(surface, self.color, (i * dis + 1, j * dis + 1, dis - 2, dis - 2))

        # Eyes
        if eyes:
            center = dis // 2
            radius = 3
            circle_middle = (i * dis + center - radius, j * dis + 8)
            circle_middle_2 = (i * dis + dis - radius * 2, j * dis + 8)
            pygame.draw.circle(surface, (0, 0, 0), circle_middle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circle_middle_2, radius)


class snake(object):
    body = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirx = 0
        self.diry = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirx = -1
                    self.diry = 0
                    self.turns[self.head.pos[:]] = [self.dirx, self.diry]

                elif keys[pygame.K_RIGHT]:
                    self.dirx = 1
                    self.diry = 0
                    self.turns[self.head.pos[:]] = [self.dirx, self.diry]

                elif keys[pygame.K_UP]:
                    self.dirx = 0
                    self.diry = -1
                    self.turns[self.head.pos[:]] = [self.dirx, self.diry]

                elif keys[pygame.K_DOWN]:
                    self.dirx = 0
                    self.diry = 1
                    self.turns[self.head.pos[:]] = [self.dirx, self.diry]

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0, turn[1]])
                if i == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                if c.dirx == -1 and c.pos[0] <= 0:
                    c.pos = (c.rows - 1, c.pos[1])
                elif c.dirx == 1 and c.pos[0] >= c.rows - 1:
                    c.pos = (0, c.pos[1])
                elif c.diry == 1 and c.pos[1] >= c.rows - 1:
                    c.pos = (c.pos[0], 0)
                elif c.diry == -1 and c.pos[1] <= 0:
                    c.pos = (c.pos[0], c.rows - 1)
                else:
                    c.move(c.dirx, c.diry)

    def reset(self, pos):
        pass

    def add_cube(self):
        pass

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)


def draw_grid(w, rows, surface):
    # Size of grid
    sizebtwn = w // rows

    x = 0
    y = 0
    for i in range(rows):
        x = x + sizebtwn
        y = y + sizebtwn

        # drawing a line
        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))


def redraw_window(surface):
    global width, rows, s
    surface.fill((0, 0, 0))
    s.draw(surface)
    draw_grid(width, rows, surface)

    # Update the Board
    pygame.display.update()


def random_snack(rows, items):
    pass


def message_box(subject, content):
    pass


def main():
    global width, rows, s
    width = 500
    rows = 20
    board = pygame.display.set_mode((width, width))
    s = snake((255, 0, 0), (10, 10))

    clock = pygame.time.Clock()

    while True:
        pygame.time.delay(80)
        clock.tick(10)
        s.move()
        redraw_window(board)

    pass


main()
