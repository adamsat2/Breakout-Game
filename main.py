import time
import random
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Breakout")
screen.tracer(0)

game_is_on = True

# x and y coordinates where the ball hits the wall
BALL_X_WALL = (SCREEN_WIDTH / 2) - 20
BALL_Y_WALL = (SCREEN_HEIGHT / 2) - 120  # remove additional 100 to take scoreboard into consideration

# y coordinate of the paddle
PADDLE_Y = ((SCREEN_HEIGHT / 2) - 50) * -1

START_LIVES = 5
lives = START_LIVES

# Uniform brick size
BRICK_LEN = 3   # width  ~ BRICK_LEN * 20 px
BRICK_WID = 1   # height ~ BRICK_WID * 20 px
brick_w = BRICK_LEN * 20
brick_h = BRICK_WID * 20

# Keep bricks fully on-screen
start_x = -SCREEN_WIDTH // 2 + brick_w // 2
end_x = SCREEN_WIDTH // 2 - brick_w // 2
start_y = 300 - brick_h // 2
end_y = 100 + brick_h // 2

colors = ["red", "orange", "yellow", "green", "cyan", "magenta", "purple", "blue"]
target_paddles = []


def place_target_paddles():
    y = start_y
    while y >= end_y:
        x = start_x
        while x <= end_x:
            p = Paddle((x, y), random.choice(colors))
            p.shapesize(stretch_wid=BRICK_WID, stretch_len=BRICK_LEN)
            target_paddles.append(p)
            x += brick_w
        y -= brick_h


def clear_target_paddles():
    for t in target_paddles:
        t.hideturtle()
        t.clear()

    target_paddles.clear()


paddle = Paddle((0, PADDLE_Y), "white")
ball = Ball()
scoreboard = Scoreboard(lives)

screen.listen()
screen.onkeypress(paddle.go_right, "d")
screen.onkeypress(paddle.go_left, "a")

while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    # Out of lives or cleared all the target paddles/we haven't initialized target paddles yet
    if lives == 0 or len(target_paddles) == 0:
        clear_target_paddles()
        place_target_paddles()
        lives = START_LIVES
        scoreboard.set_lives(lives)
        scoreboard.reset_points()
        ball.reset_position() # reset the ball position as part of starting a new game

    # Collision with target paddles
    # tar_paddle runs on a copy of target_paddles to not miss any target paddle if we remove one
    for tar_paddle in target_paddles[:]:
        if ball.distance(tar_paddle) < 30:
            ball.bounce_y()
            tar_paddle.hideturtle()
            tar_paddle.clear()
            target_paddles.remove(tar_paddle)
            scoreboard.update_points()

    # Collision with wall on x-axis
    if ball.xcor() > BALL_X_WALL or ball.xcor() < (BALL_X_WALL * -1):
        ball.bounce_x()

    # Collision with top wall or with player paddle
    if ball.ycor() > BALL_Y_WALL or (ball.ycor() < (PADDLE_Y + 30) and ball.distance(paddle) < 50):
        ball.bounce_y()

    # Outside of height (player paddle failed to catch the ball)
    if ball.ycor() < (PADDLE_Y - 30):
        ball.reset_position()
        lives -= 1
        scoreboard.update_lives()
        paddle.goto(0, PADDLE_Y)

screen.exitonclick()
