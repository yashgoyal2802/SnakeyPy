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
    def __init__(self, color, pos):
        pass

    def reset(self, pos):
        pass

    def add_cube(self):
        pass

    def draw(self, surface):
        pass


def draw_grid(w, rows, surface):
    pass


def redraw_window(surface):
    draw_grid(surface)

    # Update the Board
    pygame.display.update()


def random_snack(rows, items):
    pass


def message_box(subject, content):
    pass


def main():
    width = 500
    height = 500
    rows = 20
    board = pygame.display.set_mode((width, height))
    s = snake((255, 0, 0), (10, 10))

    clock = pygame.time.Clock()

    while True:
        pygame.time.delay(50)
        clock.tick(10)
        redraw_window(board)

    pass

