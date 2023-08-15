from turtle import Screen
from cannon import Cannon
from laser import Laser
from invaders import Invaders
from scoreboard import Scoreboard
import time
import pygame
from customtkinter import *
from tkinter import *


def start_game():
    instructions_window.destroy()

    def fire_laser():
        cannon_pos = (cannon.xcor(), cannon.ycor())
        if not laser.fired:
            laser.fire(cannon_pos)
            play_laser_sound()

    def move_laser():
        if laser.fired:
            new_y = laser.ycor() + laser.move_speed
            laser.goto(laser.xcor(), new_y)
            if laser.distance(invaders.mystery_ship) < 30:
                invaders.remove_mystery_ship()
                scoreboard.mystery_ship_score()
                play_collision_sound()
                laser.ht()
                laser.fired = False
            for ten_pt_alien in invaders.ten_aliens:
                if laser.distance(ten_pt_alien) < 15:
                    play_collision_sound()
                    ten_pt_alien.ht()
                    invaders.ten_aliens.remove(ten_pt_alien)
                    scoreboard.ten_score()
                    laser.ht()
                    laser.fired = False
                    break
            for twenty_pt_alien in invaders.twenty_aliens:
                if laser.distance(twenty_pt_alien) < 15:
                    play_collision_sound()
                    twenty_pt_alien.ht()
                    invaders.twenty_aliens.remove(twenty_pt_alien)
                    scoreboard.twenty_score()
                    laser.ht()
                    laser.fired = False
                    break
            for thirty_pt_alien in invaders.thirty_aliens:
                if laser.distance(thirty_pt_alien) < 15:
                    play_collision_sound()
                    thirty_pt_alien.ht()
                    invaders.thirty_aliens.remove(thirty_pt_alien)
                    scoreboard.thirty_score()
                    laser.ht()
                    laser.fired = False
                    break
            if laser.ycor() > 185:
                laser.ht()
                laser.fired = False
                laser.goto(cannon.xcor(), cannon.ycor())
        screen.ontimer(move_laser, 1)

    pygame.init()
    laser_sound = pygame.mixer.Sound("sound/laser.wav")
    collision_sound = pygame.mixer.Sound("sound/collision.wav")
    game_over_sound = pygame.mixer.Sound("sound/game_over.wav")
    bg_music = pygame.mixer.Sound("sound/bg_music.wav")

    game_over_sound.set_volume(3)
    bg_music.set_volume(.5)
    collision_sound.set_volume(.2)

    bg_channel = pygame.mixer.Channel(0)
    bg_channel.play(bg_music, loops=-1)

    def play_laser_sound():
        pygame.mixer.Channel(1).play(laser_sound)

    def play_collision_sound():
        pygame.mixer.Channel(2).play(collision_sound)

    def play_game_over_sound():
        bg_channel.stop()
        pygame.mixer.Channel(3).play(game_over_sound)

    screen = Screen()
    screen.tracer(0)
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Space Invaders")

    cannon = Cannon()
    invaders = Invaders()
    scoreboard = Scoreboard()
    laser = Laser()

    screen.onkey(cannon.move_left, "Left")
    screen.onkey(cannon.move_right, "Right")
    screen.onkeypress(fire_laser, "space")

    screen.listen()

    move_laser()

    playing = True
    lives = 3

    while playing:
        time.sleep(.15)
        screen.update()
        invaders.move_invaders()
        invaders.fire_missiles(screen)

        if invaders.right_most_alien.ycor() < -50 or invaders.left_most_alien.ycor() < -50:
            invaders.mystery_ship_appeared = True
            invaders.add_mystery_ship()

        # Detect missiles colliding with cannon
        for missile in invaders.missiles:
            if cannon.distance(missile) < 15:
                collision_sound.play()
                missile.ht()
                invaders.missiles.remove(missile)
                lives -= 1
                scoreboard.decrease_lives()
                time.sleep(1)

        # GAME OVER CONDITIONS
        # 1. Run out of lives
        if lives == 0:
            play_game_over_sound()
            scoreboard.reset()
            scoreboard.game_over()
            playing = False
        # 2. Aliens reach the bottom of the screen where cannon is
        for alien_type in invaders.aliens_list:
            for alien in alien_type:
                if alien.ycor() < -275:
                    play_game_over_sound()
                    scoreboard.reset()
                    scoreboard.game_over()
                    playing = False
    screen.mainloop()


instructions_window = Tk()
instructions_window.title("Space Invaders: How to Play")


instructions = "Welcome to Space Invaders!\n\nHow to Play:\n1. Use the left and right arrows to move the laser cannon "\
               "left and right across the screen.\n2. Use the space button to fire the laser at the invaders.\nOnly " \
               "one laser can be fired a time.\n3.There are 3 types of alien invaders, worth 10, 20, and 30 points " \
               "respectively.\nThey are dropping missiles as they move across the screen.\nIf a missile hits your " \
               "laser cannon, you lose a life.\nYou have 3 lives in the game.\n4. At some point in the game, " \
               "a mystery ship will appear on the screen that is worth a significant amount of points.\nIt will only " \
               "cross the screen one time.\n5. The game will end if the invaders reach the level of your " \
               "cannon.\nGood luck!"

instructions_label = CTkLabel(master=instructions_window, text=instructions)
instructions_label.grid(row=0, column=0)

start_button = CTkButton(master=instructions_window, text="Start Game", command=start_game)
start_button.grid(row=1, column=0)

instructions_window.mainloop()
