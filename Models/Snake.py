###########################
# Create by Gil Sosa Juan #
# 12 September 2021 09:40 #
###########################

from dataclasses import dataclass
from Models.Board import Board

@dataclass
class Snake:
    color : tuple
    block : int
    length: int
    speed : int
    head  : list
    body  : list

    def the_body(self, x1, y1):
        # Expresa donde esta parada la cabeza
        self.head.append(x1)
        self.head.append(y1)
        self.body.append(self.head)

    def eat(self, board: Board):
        for x in self.body:
            board.new_pos(self.color, x[0], x[1])
