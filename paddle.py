from turtle import Turtle, Screen

class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_len=4)
        self.setheading(90)
        self.penup()
        self.goto(pos)

    def player_up(self):
        self.forward(30)

    def player_down(self):
        self.backward(30)

    # def player_2_up(self):
    #     self.player_2_Paddle.forward(10)
    #
    # def player_2_down(self):
    #     self.player_2_Paddle.backward(10)


