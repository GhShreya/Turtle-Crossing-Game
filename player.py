from turtle import Turtle
FINISH_LINE = 280
FONT = ("Courier", 20, "normal")


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pencolor("DarkSlateGrey")
        self.fillcolor("DarkSeaGreen4")
        self.penup()
        self.left(90)
        self.goto(0, -280)

    def go_up(self):
        self.forward(10)

    def win(self):
        if self.ycor() > FINISH_LINE:
            self.goto(-40, -20)
            # self.write(arg="Level up!", font=FONT)
            # self.clear()
            self.goto(0, -280)
