from turtle import Turtle

FONT = ("Courier", 25, "normal")

class Scoreboard:
    def __init__(self):
        self.score = Turtle("blank")
        self.score.penup()
        self.score.ht()
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.points = 0
        self.score.goto((-390, 250))
        self.score.color("white")
        self.score.write(f"SCORE:{self.points} | HIGH SCORE:{self.high_score}", move=False, font=FONT, align="left")
        self.lives = Turtle("blank")
        self.lives.penup()
        self.lives.ht()
        self.num_lives = 3
        self.lives.goto((200, 250))
        self.lives.color("white")
        self.lives.write(f"LIVES: {self.num_lives}", move=False, font=FONT, align="left")
        self.game_over_text = Turtle("blank")
        self.game_over_text.penup()
        self.game_over_text.ht()
        self.game_over_text.color("white")

    def reset(self):
        if self.points > self.high_score:
            self.high_score = self.points
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score.clear()
        self.score.write(f"SCORE:{self.points} | HIGH SCORE:{self.high_score}", move=False, font=FONT, align="left")
        self.score.ht()
        self.points = 0

    def game_over(self):
        self.game_over_text.goto((0, 200))
        self.game_over_text.write("GAME OVER", move=False, font=("Courier", 35, "bold"), align="center")
        self.game_over_text.ht()

    def decrease_lives(self):
        self.lives.clear()
        self.num_lives -= 1
        self.lives.write(f"LIVES: {self.num_lives}", move=False, font=FONT, align="left")
        self.lives.ht()

    def ten_score(self):
        self.score.clear()
        self.points += 10
        self.score.write(f"SCORE:{self.points} | HIGH SCORE:{self.high_score}", move=False, font=FONT, align="left")
        self.score.ht()

    def twenty_score(self):
        self.score.clear()
        self.points += 20
        self.score.write(f"SCORE:{self.points} | HIGH SCORE:{self.high_score}", move=False, font=FONT, align="left")
        self.score.ht()

    def thirty_score(self):
        self.score.clear()
        self.points += 30
        self.score.write(f"SCORE:{self.points} | HIGH SCORE:{self.high_score}", move=False, font=FONT, align="left")
        self.score.ht()

    def mystery_ship_score(self):
        self.score.clear()
        self.points += 200
        self.score.write(f"SCORE:{self.points} | HIGH SCORE:{self.high_score}", move=False, font=FONT, align="left")
        self.score.ht()
