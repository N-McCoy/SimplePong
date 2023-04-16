#create screen
# make and move paddle
# make 2nd paddle
# make and move ball
# wall collision and bounce
# paddle collision
# missed paddle
# score

from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from Scoreboard import Scoreboard


screen = Screen()
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)
screen.setup(width=1000, height=600)

ball = Ball()
scoreboard = Scoreboard()
player_1_Paddle = Paddle((475, 0))
player_2_Paddle = Paddle((-475, 0))

screen.listen()
screen.onkeypress(player_1_Paddle.player_up, 'Up')
screen.onkeypress(player_1_Paddle.player_down, 'Down')
screen.onkeypress(player_2_Paddle.player_up, 'w')
screen.onkeypress(player_2_Paddle.player_down, 's')

gameIsOn = True
sleep_time = 0.05
while gameIsOn:
    ball.ball_move()
    scoreboard.update_scoreboard()
    screen.update()
    time.sleep(sleep_time)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    if ball.distance(player_1_Paddle) < 60 and ball.xcor() > 445 or ball.distance(player_2_Paddle) < 60 and ball.xcor() < -445:
        ball.paddle_bounce()
        if sleep_time > 0.005:
            sleep_time -= 0.002
    if ball.xcor() > 480 or ball.xcor() < -480:
        scoreboard.add_point(ball.xcor())
        ball.goal()
        sleep_time = 0.05

screen.exitonclick()