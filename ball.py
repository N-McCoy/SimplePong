from turtle import Turtle
from random import randint
exclude = [0]
exclude_x = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3,  4, 5, 6, 7, 8, 9]
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.move_x = 10
        self.move_y = 10
        #self.setheading(randint(0, 359))


    # def start_x(self):
    #     rand_x = 0
    #     while rand_x in exclude_x:
    #         rand_x = randint(-10, 10)
    #     return rand_x
    #
    # def start_y(self):
    #     rand_y = 0
    #     while rand_y in exclude:
    #         rand_y = randint(-15, 15)
    #     return rand_y
    #
    #
    def ball_move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.move_y *= -1

    def paddle_bounce(self):
        self.move_x *= -1



    def goal(self):
        self.goto(0, 0)
        self.move_y *= -1
        self.move_y += randint(-7, 7)
        self.move_x = 10
        self.move_x *= -1













    # def ball_move(self):
    #     self.forward(10)
    #
    # def wall_bounce(self):
    #     current_heading = self.heading()
    #     if 45 >= current_heading > 0:
    #         self.setheading(randint(325, 349))
    #     elif 90 >= current_heading > 45:
    #         self.setheading(randint(280, 305))
    #     elif 135 >= current_heading > 90:
    #         self.setheading((randint(235, 260)))
    #     elif 180 >= current_heading > 135:
    #         self.setheading(randint(190, 215))
    #     elif 225 >= current_heading > 180:
    #         self.setheading(randint(145, 170))
    #     elif 270 >= current_heading > 225:
    #         self.setheading(randint(100, 125))
    #     elif 315 >= current_heading > 270:
    #         self.setheading(randint(55, 80))
    #     elif 359 >= current_heading > 315:
    #         self.setheading(randint(10, 35))
    #
    # def paddle_bounce(self):
    #     current_heading = self.heading()
    #     if 45 >= current_heading > 0:
    #         self.setheading(randint(135, 180))
    #     elif 90 >= current_heading > 45:
    #         self.setheading(randint(90, 135))
    #     elif 135 >= current_heading > 90:
    #         self.setheading((randint(225, 270)))
    #     elif 180 >= current_heading > 135:
    #         self.setheading(randint(0, 45))
    #     elif 225 >= current_heading > 180:
    #         self.setheading(randint(315, 359))
    #     elif 270 >= current_heading > 225:
    #         self.setheading(randint(270, 315))
    #     elif 315 >= current_heading > 270:
    #         self.setheading(randint(225, 270))
    #     elif 359 >= current_heading > 315:
    #         self.setheading(randint(180, 225))