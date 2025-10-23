from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color(color)
        self.penup()
        self.goto(position)

    def go_right(self):
        if self.xcor() < 350:
            new_x = self.xcor() + 20
            self.goto(new_x, self.ycor())

    def go_left(self):
        if self.xcor() > -350:
            new_x = self.xcor() - 20
            self.goto(new_x, self.ycor())
