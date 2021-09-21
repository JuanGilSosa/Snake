###########################
# Create by Gil Sosa Juan #
# 12 September 2021 09:34 #
###########################

from Models.Snake import Snake
from Models.Board import Board
import pygame as pg

if __name__ == '__main__':
    snake = Snake((0, 0, 0), 2)
    board = Board(snake.color)

    x1 = 100
    y1 = 100

    x1_change = 0
    y1_change = 0



    clock = pg.time.Clock()

    while True:
        # Este bucle for, es el ciclo del juego, todos lo tienen
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                if event.key == pg.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                if event.key == pg.K_UP:
                    y1_change = -10
                    x1_change = 0
                if event.key == pg.K_DOWN:
                    y1_change = +10
                    x1_change = 0

        x1 += x1_change
        y1 += y1_change

        # seteamos color, para que cuando se realice el movimiento de la serpiente
        # no deje rastro, si es que no posee length

        #for i in range(snake.length):
        #    board.new_pos(snake.color, x1 - 10, y1)
        #    if i == snake.length:
        #        board.set_fill((255, 255, 255))

        board.new_pos(snake.color, x1, y1)

        board.update_()

        # Este metodo representarian los FPS del juego
        clock.tick(10)