###########################
# Create by Gil Sosa Juan #
# 12 September 2021 09:40 #
###########################

from Models.Board import Board

class Snake:
    def __init__(self, color: tuple,
                 block: int,
                 length: int,
                 speed: int,
                 head: list, body: list
                 ):
        self.color = color
        self.block = block
        self.length = length
        self.speed = speed
        self.head = head
        self.body = body

    def the_body(self, x1, y1):
        # Expresa donde esta parada la cabeza
        self.head.append(x1)
        self.head.append(y1)
        print(self.head)
        self.body.append(self.head)

    def eat(self, board: Board):
        for x in self.body:
            board.draw(self.color, x[0], x[1])
