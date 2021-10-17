from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue"]


class BlockManager:

    def __init__(self):
        self.all_blocks = []
        self.number_of_blocks = 15

    def create_block(self):

        block_x_pos = -700
        block_y_pos = 400
        block_size = 1300 / self.number_of_blocks

        for color in COLORS:
            for block in range(0, self.number_of_blocks):
                new_block = Turtle("square")
                new_block.speed(0)
                new_block.shapesize(stretch_wid=3, stretch_len=4)
                new_block.penup()
                new_block.color(color)
                new_block.goto(block_x_pos, block_y_pos)
                self.all_blocks.append(new_block)

                block_x_pos += 100

            block_x_pos = -700
            block_y_pos -= 90

    def delete_block(self, block):
        block.color("black")
        self.all_blocks.remove(block)
