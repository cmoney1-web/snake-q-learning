from turtle import Turtle
import random

GRID_SIZE = 20
MIN_POSITION = -260
MAX_POSITION = 260


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        positions = range(
            MIN_POSITION,
            MAX_POSITION + GRID_SIZE,
            GRID_SIZE
        )

        random_x = random.choice(positions)
        random_y = random.choice(positions)

        self.goto(random_x, random_y)