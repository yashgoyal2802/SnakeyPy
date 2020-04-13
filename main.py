import pygame
from tkinter import *
import math
import random


class cube(object):
    rows = 0
    w = 0

    def __init__(self, start, dirx=1, diry=0, color=(255, 0, 0)):
        pass

    def move(self, dirx, diry):
        pass

    def draw(self, surface, eyes=False):
        pass


class snake(object):
    body = []
    turns = ()

    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirx = 0
        self.diry = 1

    def reset(self, pos):
        pass

    def add_cube(self):
        pass

    def draw(self, surface):
        pass


def draw_grid(w, rows, surface):
    # Size of grid
    sizebtwn = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizebtwn
        y = y + sizebtwn

        # drawing a line
        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))


def redraw_window(surface):
    global width, rows
    surface.fill((0, 0, 0))
    draw_grid(width, rows, surface)

    # Update the Board
    pygame.display.update()


def random_snack(rows, items):
    pass


def message_box(subject, content):
    pass


def main():
    global width, rows
    width = 500
    rows = 20
    board = pygame.display.set_mode((width, width))
    # s = snake((255, 0, 0), (10, 10))

    clock = pygame.time.Clock()

    while True:
        pygame.time.delay(80)
        clock.tick(10)
        redraw_window(board)


main()
