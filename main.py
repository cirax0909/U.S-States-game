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
    answer_state = screen.textinput(title=f"Correct answer {right_state}/50", prompt="Enter a state").title()
    states_file = pandas.read_csv("50_states.csv")
    us_states = states_file.state.to_list()
    if answer_state == "Exit":
        missing_state = [state for state in us_states if state not in us_states]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("missing states.csv")
        break

    for state in us_states:
        if answer_state == state:
            a = int(states_file.x[states_file["state"] == answer_state])
            b = int(states_file.y[states_file.state == answer_state])
            display.display(a, b, answer_state)
            if answer_state not in already_taken:
                right_state += 1
                already_taken.append(answer_state)

screen.exitonclick()
