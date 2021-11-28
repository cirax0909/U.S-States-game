import turtle
import pandas
from display_state import Display

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
right_state = 0
already_taken = []

display = Display()

while right_state <= 50:
    answer_state = screen.textinput(title=f"Correct answer {right_state}/50", prompt="Enter a state")
    already_taken.append(answer_state)
    print(already_taken)
    states_file = pandas.read_csv("50_states.csv")
    us_states = states_file.state

    for state in us_states:
        if answer_state not in already_taken and answer_state == state:
            a = int(states_file.x[states_file["state"] == answer_state])
            b = int(states_file.y[states_file.state == answer_state])
            display.display(a, b, answer_state)
            right_state += 1

screen.exitonclick()
