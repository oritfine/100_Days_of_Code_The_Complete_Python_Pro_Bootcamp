import random
import turtle
import colorgram
from turtle import Turtle, Screen
turtle.colormode(255)


def generate_rgb_colors_from_image(image_name, num_of_colors):
    colors = colorgram.extract(image_name, num_of_colors)
    colors = [c.rgb[:] for c in colors]
    print(colors)


if __name__ == '__main__':
    generate_rgb_colors_from_image('image.jpg', 30)

    colors = [(236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216),
              (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177),
              (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28),
              (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199),
              (179, 17, 8), (233, 66, 34)]

    t = Turtle()
    width = t.screen.window_width()
    height = t.screen.window_height()
    dot_size = 20
    pos = t.pos()
    i = 1
    while pos[1] < height//2 - 50:
        t.teleport(-width//2 + 50, -height//2 + i*50)
        i += 1
        pos = t.pos()
        while pos[0] < width//2 - 50:
            t.dot(dot_size, random.choice(colors))
            pos = t.pos()
            t.teleport(pos[0] + 50)

    screen = Screen()
    screen.exitonclick()


