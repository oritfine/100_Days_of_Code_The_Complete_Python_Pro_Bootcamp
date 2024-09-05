import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)

if __name__ == '__main__':
    is_race_on = False
    colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Pink"]
    screen = Screen()
    screen.setup(width=500, height=400)
    user_bet = screen.textinput("Turtle Race", f"Choose a color for your candidate in the race: \n"
                                               f"{' / '.join(colors)}").title()

    turtles = []
    y = -120
    for c in colors:
        t = Turtle(shape="turtle")
        t.color(c)
        t.penup()
        t.goto(-230, y)
        y += 40
        turtles.append(t)

    if user_bet in colors:
        is_race_on = True
    while is_race_on:
        for t in turtles:
            if t.xcor() > 230:
                is_race_on = False
            t.forward(random.randint(0, 10))

    winning_color = []
    max_x = 0
    for t in turtles:
        if t.xcor() > max_x and t.xcor() > 230:
            max_x = t.xcor()
            winning_color = [t.pencolor()]
        elif t.xcor() == max_x:
            winning_color.append(t.pencolor())
    if user_bet in winning_color:
        print("You Win!")
    else:
        print("You Lose!")
    if len(winning_color) == 1:
        print(f"The winning turtle: {winning_color[0]}.")
    else:
        print(f"The winning turtles: {' , '.join(winning_color)}.")
    screen.exitonclick()
