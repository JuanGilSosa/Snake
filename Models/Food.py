import random


class Food:
    foodX = 0
    foodY = 0
    color = (0, 0, 255)

    def __init__(self, dis_width, dis_height, snake_block):
        self.random(dis_width, dis_height, snake_block)

    def random(self, dis_width, dis_height, snake_block):
        self.foodX = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        self.foodY = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
