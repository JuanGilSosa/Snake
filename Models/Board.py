###########################
# Create by Gil Sosa Juan #
# 12 September 2021 10:22 #
###########################
import pygame as pg


class Board:

    def __init__(self, width: int, height: int):
        pg.init()
        pg.font.init()
        pg.display.set_caption("VIBORITA")
        self.__myfont = pg.font.SysFont('Agency FB Bold', 30)
        self.__width = width
        self.__height = height
        self.__surface = pg.display.set_mode((self.__width, self.__height))
        self.__surface.fill((255, 255, 255))
        self.update_()

    def update_(self):
        pg.display.update()

    def draw(self, color_snake: tuple, pos_x: float, pos_y: float):
        pg.draw.rect(self.__surface, color_snake, [pos_x, pos_y, 10, 10])

    def draw_text(self, color: tuple, pos_x: float, pos_y: float, points: int):
        text = self.__myfont.render(f'Puntaje: {points}', False, (0, 0, 0))
        self.__surface.blit(text, (20, 0))

    # Setea el color del background
    def set_fill(self, color: tuple):
        self.__surface.fill(color)

    def get_width(self) -> int:
        return self.__width

    def get_height(self) -> int:
        return self.__height

    def get_surface(self) -> pg.Surface:
        return self.__surface

    def draw_border(self):
        # x = 600 y = 400
        # line(surface, color, start_pos, end_pos, width)

        # Left
        pg.draw.line(self.__surface, (0, 0, 0), (20, 20), (20, 380), 1)
        # Down
        pg.draw.line(self.__surface, (0, 0, 0), (20, 380), (580, 380), 1)
        # Right
        pg.draw.line(self.__surface, (0, 0, 0), (580, 380), (580, 20), 1)
        # Up
        pg.draw.line(self.__surface, (0, 0, 0), (580, 20), (20, 20), 1)
