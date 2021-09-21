import pygame as pg
from Models.Board import Board
from Models.Snake import Snake

class App:
    def __init__(self):
        pass

    def start(self):
        snake = Snake((0, 0, 0), 2)
        board = Board(snake.color)

        x1 = 100
        y1 = 100

        x1_change = 0
        y1_change = 0

        clock = pg.time.Clock()

        # Le asignamos un valor para obtener la tecla presionada
        key_pressed = None
        while True:

            # Este bucle for, es el ciclo del juego, todos lo tienen
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                if event.type == pg.KEYDOWN:
                    print(key_pressed)
                    if (event.key == pg.K_LEFT) and (key_pressed != pg.K_RIGHT):
                        key_pressed = pg.K_LEFT
                        x1_change = -10
                        y1_change = 0
                    if (event.key == pg.K_RIGHT) and (key_pressed != pg.K_LEFT):
                        key_pressed = pg.K_RIGHT
                        x1_change = 10
                        y1_change = 0
                    if (event.key == pg.K_UP) and (key_pressed != pg.K_DOWN):
                        key_pressed = pg.K_UP
                        y1_change = -10
                        x1_change = 0
                    if (event.key == pg.K_DOWN) and (key_pressed != pg.K_UP):
                        key_pressed = pg.K_DOWN
                        y1_change = +10
                        x1_change = 0

            x1 += x1_change
            y1 += y1_change

            # seteamos color, para que cuando se realice el movimiento de la serpiente
            board.set_fill((255, 255, 255))
            board.new_pos(snake.color, x1, y1)

            board.update_()

            # Este metodo representarian los FPS del juego
            clock.tick(10)