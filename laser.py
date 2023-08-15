from turtle import Turtle


class Laser(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()
        self.ht()
        self.shapesize(.5, .25)
        self.move_speed = 20
        self.fired = False

    def fire(self, cannon_pos):
        self.goto(cannon_pos)
        self.fired = True
        if self.fired:
            new_y = self.ycor() + self.move_speed
            self.goto(self.xcor(), new_y)
            self.st()

