from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 240)
        self.write(arg=f"Level:{self.level}", align="left", font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(arg=f"Level:{self.level}", align="left", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(-100, -20)
        self.write(arg=f"Game Over!\n Score:{self.level - 1}\n Level:{self.level}", font=FONT)
