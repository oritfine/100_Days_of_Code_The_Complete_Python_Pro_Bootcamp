import turtle
from prettytable import PrettyTable

t = turtle.Turtle()
t.shape('turtle')
t.color('red', 'green')
for i in range(100):
    t.forward(1)


screen = turtle.Screen()
screen.exitonclick()

table = PrettyTable()
table.add_column("Pokemon Name", ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column("Type", ['Electric', 'Water', 'Fire'])
table.align = "l"
print(table)
