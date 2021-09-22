import pygame as pg
from Models.Board import Board
from Models.Snake import Snake
from Models.Food import Food

class App:
    def __init__(self):
        pass

    def start(self):
        snake = Snake((0, 0, 0), 10, 0, 10, [], [])
        board = Board(snake.color)
        food  = Food(board.get_width(), board.get_height(), snake.block)
        x1 = board.get_width() / 2
        y1 = board.get_height() / 2

        x1_change = 0
        y1_change = 0

        clock = pg.time.Clock()

        # Le asignamos un valor para obtener la tecla presionada
        key_pressed = None

        game_over = False

        while not game_over:
            # Este bucle for, es el ciclo del juego, todos lo tienen
            board.update_()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                if event.type == pg.KEYDOWN:
                    print("Key Value = ", key_pressed)
                    if (event.key == pg.K_LEFT) and (key_pressed != pg.K_RIGHT):
                        key_pressed = pg.K_LEFT
                        x1_change = -snake.block
                        y1_change = 0
                    if (event.key == pg.K_RIGHT) and (key_pressed != pg.K_LEFT):
                        key_pressed = pg.K_RIGHT
                        x1_change = snake.block
                        y1_change = 0
                    if (event.key == pg.K_UP) and (key_pressed != pg.K_DOWN):
                        key_pressed = pg.K_UP
                        y1_change = -snake.block
                        x1_change = 0
                    if (event.key == pg.K_DOWN) and (key_pressed != pg.K_UP):
                        key_pressed = pg.K_DOWN
                        y1_change = +snake.block
                        x1_change = 0

            # Game Over?
            if x1 > board.get_width() or x1 < 0 or y1 > board.get_height() or y1 < 0:
                game_over = True

            x1 += x1_change
            y1 += y1_change

            # seteamos color, para que cuando se realice el movimiento de la serpiente
            board.set_fill((255, 255, 255))
            board.draw(food.color, food.foodX, food.foodY) # food
            board.draw(snake.color, x1, y1) # snake

            snake.the_body(x1, y1)
            if len(snake.body) > snake.length:
                del snake.body[0]

            for x in snake.body[:-1]:
                if x == snake.head:
                    game_over = True

            snake.eat(board)

            board.update_()
            if x1 == food.foodX and y1 == food.foodY:
                food.random(board.get_width(), board.get_height(), snake.block)
                print("BUEN PROVECHO")

            # Este método representarían los FPS del juego
            clock.tick(snake.speed)