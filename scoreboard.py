from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, lives):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = lives
        self.update_scoreboard()

    def scoreboard_boarder(self):
        self.goto(-400, 300)
        self.pendown()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(400, 300)
        self.penup()

    def update_scoreboard(self):
        self.clear()
        self.scoreboard_boarder()
        self.goto(-100, 300)
        self.write(self.score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 300)
        self.write(self.lives, align="center", font=("Courier", 80, "normal"))

    def update_points(self):
        self.score += 1
        self.update_scoreboard()

    def reset_points(self):
        self.score = 0
        self.update_scoreboard()

    def update_lives(self):
        self.lives -= 1
        self.update_scoreboard()

    def set_lives(self, lives):
        self.lives = lives
        self.update_scoreboard()