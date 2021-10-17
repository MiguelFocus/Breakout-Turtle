from turtle import Screen
from blocks import BlockManager
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(height=1000, width=1550)
screen.bgcolor("black")
screen.title("BreakOut")
screen.tracer(0)

blockmanager = BlockManager()
blockmanager.create_block()
paddle = Paddle()
ball = Ball()


screen.listen()
screen.onkey(paddle.go_left, "a")
screen.onkey(paddle.go_right, "d")


game_is_on = True

while game_is_on:
    # time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.xcor() >= 750 or ball.xcor() <= -750:
        ball.bounce_x()

    if ball.ycor() == -500:
        ball.reset_position(paddle.xcor())

    if ball.ycor() == 500:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle) <70:
        ball.bounce_y()

    # Detect collision with block an delete block
    for block in blockmanager.all_blocks:
        if ball.distance(block) < 100:
            # ball.bounce_x()
            ball.bounce_y()
            blockmanager.delete_block(block)


