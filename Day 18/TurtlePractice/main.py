import turtle
from turtle import Turtle, Screen
import random


def draw_square():
    t = Turtle()
    for i in range(4):
        t.forward(70)
        t.right(90)


def draw_dashed_line():
    t = Turtle()
    for _ in range(20):
        t.forward(5)
        pos = t.pos()
        t.teleport(pos[0] + 10)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def draw_shape(size, t):
    t.color(random_color())
    for _ in range(size):
        t.forward(100)
        t.right(360 / size)


def draw_shapes():
    t = Turtle()
    for size in range(3, 11):
        draw_shape(size, t)


def draw_random_walk():
    t = Turtle()
    t.width(15)
    t.speed(8)
    angles = [0, 90, 180, 270]
    for _ in range(200):
        t.color(random_color())
        t.setheading(random.choice(angles))
        t.forward(20)


def draw_spirograph(size_of_gap):
    t = Turtle()
    t.speed('fastest')
    for i in range(360 // size_of_gap):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + size_of_gap)


if __name__ == '__main__':
    turtle.colormode(255)
    # draw_shapes()
    # draw_random_walk()
    draw_spirograph(2)
    screen = Screen()
    screen.exitonclick()
