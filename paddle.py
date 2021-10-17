from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.ycor = -450
        self.shape("square")
        self.speed(0)
        self.resizemode("user")
        self.color("white")
        self.penup()
        self.setheading(0)
        self.shapesize(stretch_wid=1, stretch_len=10, outline=0)
        self.setpos(x=0, y=self.ycor)

    def go_right(self):
        if self.xcor() < 630:
            self.forward(150)

    def go_left(self):
        if self.xcor() > -630:
            self.backward(150)