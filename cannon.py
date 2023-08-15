from turtle import Turtle, register_shape
from PIL import Image


# Resize image
# image = Image.open("cannon.gif")
# image.thumbnail((50,50))
# image.save("cannon.gif", "GIF")

class Cannon(Turtle):
    def __init__(self):
        super().__init__()
        register_shape("img/cannon.gif")
        self.shape("img/cannon.gif")
        self.penup()
        self.goto((0, -280))

    def move_left(self):
        if self.xcor() > -360:
            new_x = self.xcor() - 25
            self.goto(new_x, self.ycor())

    def move_right(self):
        if self.xcor() < 360:
            new_x = self.xcor() + 25
            self.goto(new_x, self.ycor())
