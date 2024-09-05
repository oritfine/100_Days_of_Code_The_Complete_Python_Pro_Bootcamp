import turtle
from turtle import Turtle, Screen
turtle.colormode(255)

if __name__ == '__main__':

    t = Turtle()

    def move_forward():
        t.forward(10)


    def move_backward():
        t.backward(10)


    def move_counter_clockwise():
        t.setheading(t.heading() + 10)


    def move_clockwise():
        t.setheading(t.heading() - 10)


    def clear():
        t.clear()
        t.teleport(0, 0)
        t.setheading(0)

    screen = Screen()
    screen.listen()
    screen.onkey(key="w", fun=move_forward)
    screen.onkey(key="s", fun=move_backward)
    screen.onkey(key="a", fun=move_counter_clockwise)
    screen.onkey(key="d", fun=move_clockwise)
    screen.onkey(key="c", fun=clear)

    screen.exitonclick()


