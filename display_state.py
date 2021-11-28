from turtle import Turtle
FONT = ("Courier", 18, "normal")

class Display(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.pencolor("black")

    def display(self, x, y, correct_answer):
        self.goto(x=x, y=y)
        self.write(f'{correct_answer}', move=False, align='center', font=FONT)