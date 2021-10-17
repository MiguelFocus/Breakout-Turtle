from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, -400)
        self.speed(6)
        self.x_move = 5
        self.y_move = 5


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        # if self.movspeed > 0.01:
        #     self.movspeed -= 0.005

    def reset_position(self, position):
        self.hideturtle()
        self.goto(x=position, y=-400)
        self.bounce_x()
        self.showturtle()
        # self.movspeed = 0.05