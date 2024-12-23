import random
from turtle import Turtle
color_list = [(210, 155, 100), (52, 107, 131), (176, 78, 34), (238, 245, 242), (200, 143, 33), (117, 155, 171),
              (124, 79, 98),(123, 175, 157), (50, 40, 29), (229, 197, 128), (230, 237, 240), (190, 88, 109), (11, 51, 65),
              (44, 169, 125),(195, 124, 142), (50, 125, 121), (169, 21, 29), (226, 94, 80), (243, 163, 161), (4, 28, 26),
              (37, 32, 34),(80, 148, 170), (165, 26, 22), (235, 166, 170), (101, 125, 157), (171, 206, 190), (25, 79, 88), (168, 201, 206)]
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.penup()
        self.goto(100, 100)
        self.hideturtle()
        self.b = 20
        self.c = 6
        
    def new_car(self):
        random_chance = random.randint(1, self.c)
        if random_chance == 1:
            n_c = Turtle("square")
            n_c.penup()
            n_c.shapesize(stretch_wid=1, stretch_len=2)
            n_c.pencolor(random.choice(color_list))
            n_c.fillcolor(random.choice(color_list))
            n_c.left(180)
            n_c.goto(300, random.randint(-270, 270))
            self.cars.append(n_c)

    def move(self):
        for car in self.cars:
            car.forward(random.randint(10, self.b))

    def increment(self):
        self.b += MOVE_INCREMENT
        self.c -= 1
        self.move()
