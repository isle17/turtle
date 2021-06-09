import random
from turtle import Turtle, Screen


def create_turtles(number_of_turtles):
    """Creates a list of turtles and returns the list. Designed so that we can build color and shape multiple turtle"""
    turtles = []
    for x in range(1, number_of_turtles + 1):
        turtles.append(Turtle())
    return turtles


def shape_color_turtles(list_of_turtles):
    """Takes a list of turtles and sets their shape to 'turtle' and their color to a color with a name that people
       can guess such as red, green, blue, black, orange. Turtle class has a lot of colors that are hard to identify
       such as sienna, or dark salmon """
    colors = ["red", "green", "black", "blue", "yellow", "purple"]
    index = 0
    for turtle in list_of_turtles:
        turtle.shape("turtle")
        turtle.color(colors[index])
        index += 1


def set_turtle(turtle, x, y):
    """Sets the starting point for each turtle"""
    turtle.penup()
    turtle.goto(x, y)


# def victory_condition(list):
#     """Check if any turtle has reached the finish line"""
#     for turtle in list:
#         if turtle.xcor() == 350:
#             return True
#         else:
#             return False

# Should this be broken into more functions?
def move_turtles(turtle_list):
    """Move each turtle randomly takes a list and a boolean. Booelan is used to see if the turtles have made it to the
       finish line"""
    length_turtle_list = len(turtle_list) - 1
    victory = False
    while not victory:
        random_int = random.randint(0, length_turtle_list)
        random_turtle = turtle_list[random_int]
        random_turtle.forward(10)
        for turtle in turtle_list:
            if turtle.xcor() == 350:
                return turtle

        # victory = victory_condition(turtle_list)





turtle_list = create_turtles(3)
shape_color_turtles(turtle_list)
print(turtle_list[0].color())

screen = Screen()
screen.setup(width=400, height=500)

y_coordinate = -100
for turtle in turtle_list:
    set_turtle(turtle=turtle, x=-230, y=y_coordinate)
    y_coordinate += 50

user_bet = screen.textinput(title="Place a bet!", prompt="Which turtle will win the race?: ")
# print(user_bet)
# pace turtle is used to write if you won or lost on the screen
pace_turtle = Turtle()
pace_turtle.hideturtle()
pace_turtle.penup()
pace_turtle.goto(-200, 200)

winning_turtle = move_turtles(turtle_list)

if winning_turtle.fillcolor() == user_bet:
    pace_turtle.write("Your Turtle Won!", font=("Arial", 23, "normal"))
else:
    pace_turtle.write(f"Your Turtle Lost :(  {winning_turtle.fillcolor().upper()} was the winner!",
                      font=("Arial", 23, "normal"))

screen.exitonclick()
