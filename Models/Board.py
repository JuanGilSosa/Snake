###########################
# Create by Gil Sosa Juan #
# 12 September 2021 10:22 #
###########################
import pygame as pg


class Board:
    def __init__(self, color_snake: tuple):
        pg.init()
        pg.display.set_caption("VIBORITA")
        self.__surface = pg.display.set_mode((400, 300))
        self.__surface.fill((255, 255, 255))
        self.update_()

    def update_(self):
        pg.display.update()

    def new_pos(self, color_snake: tuple, pos_x: int, pos_y: int):
        pg.draw.rect(self.__surface, color_snake, [pos_x, pos_y, 10, 10])

    # Setea el color del background
    def set_fill(self, color: tuple):
        self.__surface.fill(color)
