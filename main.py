from turtle import Screen
from player import Player
from car_manager import CarManager
import time
from scoreboard import Score
screen = Screen()
screen.tracer(0)
screen.colormode(255)
screen.setup(height=600, width=600)
screen.bgcolor("gray50")
screen.title("Turtle Crossing Game!")

play = Player()

score = Score()

car = CarManager()

screen.listen()
screen.onkeypress(fun=play.go_up, key='space')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.new_car()
    car.move()
    # Detect Collision
    for c in car.cars:           
        if c.distance(play) < 20:
            score.game_over()
            game_is_on = False
    # Detect Successful Crossing
    if play.ycor() > 280:
        play.win()
        score.level_up()
        car.increment()
screen.exitonclick()
