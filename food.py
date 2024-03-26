from turtle import Turtle
import random

fruit_colors = ['red', 'yellow', 'orange', 'purple', 'brown', 'blue', 'green']


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(random.choice(fruit_colors))
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 273)
        self.goto(random_x, random_y)

    def refresh(self):
        self.color(random.choice(fruit_colors))
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 273)
        self.goto(random_x, random_y)
