from turtle import Turtle, register_shape
import random
from PIL import Image

# Make images smaller
# image = Image.open("img/alien.gif")
# image.thumbnail((60, 60))
# image.save("img/alien.gif", "GIF")


class Invaders(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("blank")
        self.ten_aliens = []
        self.twenty_aliens = []
        self.thirty_aliens = []
        self.aliens_list = [self.ten_aliens, self.twenty_aliens, self.thirty_aliens]
        self.missiles = []
        self.move_dir = 3
        self.mystery_ship_appeared = False
        register_shape("img/alien.gif")
        self.mystery_ship = Turtle("img/alien.gif")
        self.mystery_ship.penup()
        self.mystery_ship.ht()
        self.mystery_ship.goto(-320, 110)
        self.right_most_alien = None
        self.left_most_alien = None
        self.setup_invaders()
        self.random_aliens()

    def setup_invaders(self):
        for x in range(-320, 320, 59):
            for y in range(0, 60, 30):
                register_shape("img/10px alien.gif")
                ten_alien = Turtle("img/10px alien.gif")
                ten_alien.penup()
                ten_alien.goto(x, y)
                self.ten_aliens.append(ten_alien)
        for x in range(-320, 320, 59):
            for y in range(60, 120, 30):
                register_shape("img/20px alien.gif")
                twenty_alien = Turtle("img/20px alien.gif")
                twenty_alien.penup()
                twenty_alien.goto(x, y)
                self.twenty_aliens.append(twenty_alien)
        for x in range(-320, 320, 59):
            for y in range(120, 180, 30):
                register_shape("img/30px alien.gif")
                thirty_alien = Turtle("img/30px alien.gif")
                thirty_alien.penup()
                thirty_alien.goto(x, y)
                self.thirty_aliens.append(thirty_alien)

    def add_mystery_ship(self):
        if self.mystery_ship_appeared:
            self.mystery_ship.st()
            new_x = self.mystery_ship.xcor() + 5
            self.mystery_ship.goto(new_x, self.mystery_ship.ycor())

    def remove_mystery_ship(self):
        self.mystery_ship.ht()
        self.mystery_ship.shape("blank")
        self.mystery_ship_appeared = False


    def move_invaders(self):
        for alien_type in self.aliens_list:
            for alien in alien_type:
                new_x = alien.xcor() + self.move_dir
                alien.goto(new_x, alien.ycor())

                if self.right_most_alien is None or alien.xcor() > self.right_most_alien.xcor():
                    self.right_most_alien = alien
                if self.left_most_alien is None or alien.xcor() < self.left_most_alien.xcor():
                    self.left_most_alien = alien

        if self.right_most_alien.xcor() > 380 or self.left_most_alien.xcor() < -380:
            self.move_dir *= -1
            for alien_type in self.aliens_list:
                for alien in alien_type:
                    new_y = alien.ycor() - 20
                    alien.goto(alien.xcor(), new_y)
            if self.move_dir > 0:
                self.move_dir += 1
            else:
                self.move_dir -= 1

    def random_aliens(self):
        while len(self.missiles) < 4:
            alien_type = random.choice(self.aliens_list)
            alien = random.choice(alien_type)
            missile = Turtle("triangle")
            missile.color("white")
            missile.tilt(270)
            missile.shapesize(.25, .5)
            missile.penup()
            missile.goto(alien.xcor(), alien.ycor())
            self.missiles.append(missile)

    def fire_missiles(self, screen):
        for missile in self.missiles:
            new_y = missile.ycor() - 15
            missile.goto(missile.xcor(), new_y)
            if missile.ycor() < -300:
                self.missiles.remove(missile)
                missile.clear()
                missile.ht()
        screen.ontimer(self.random_aliens, 5000)
