import turtle
import pandas

screen = turtle.Screen()
data = pandas.read_csv("28_states.csv")
screen.title("INDIA States Game")
img = "india.gif"
screen.addshape(img)
turtle.shape(img)
state_data = data.state.to_list()
guess_state = []
missed_state = []

while len(guess_state) < 28:
    answer_state = screen.textinput(title=f"{len(guess_state)}/28 Guess the State", prompt="what's another state name").title()
    guess_state.append(answer_state)
    if answer_state == "Exit":
        for n in state_data:
            if n not in guess_state:
                missed_state.append(n)
        mis_data = pandas.DataFrame(missed_state)
        mis_data.to_csv("States_that_are_Missed.csv")
        print(f"Missed States :{missed_state}")
        break

    if answer_state in state_data:
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        row = data[data['state'] == answer_state]
        t.goto(int(row.x), int(row.y))
        t.write(answer_state)
