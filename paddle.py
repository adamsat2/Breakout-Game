from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=5.2)
        self.color(color)
        self.penup()
        self.goto(position)

    def go_right(self):
        new_x = self.xcor() + 20
        # use min function to stop player from going offscreen
        self.goto(min(new_x, 348), self.ycor())

    def go_left(self):
        new_x = self.xcor() - 20
        # use max function to stop player from going offscreen
        self.goto(max(new_x, -348), self.ycor())
