import turtle
import pandas

writer_turtle = turtle.Turtle()
writer_turtle.hideturtle()
writer_turtle.penup()
screen = turtle.Screen()

scoreboard = 0

screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
data = pandas.read_csv("50_states.csv")

states_list = data["state"].to_list()
x_cor_list = data["x"].to_list()
y_cor_list = data["y"].to_list()

correct_guesses = []

game_continue = True
while game_continue:
    answer_state = screen.textinput(title=f"States guessed: ({scoreboard}/50)", prompt="What's another state's name?").title()
    for state_name in states_list:
        position = states_list.index(state_name)
        if answer_state == "Exit":
            game_continue = False
        if state_name == answer_state:
            writer_turtle.goto(x_cor_list[position], y_cor_list[position])
            writer_turtle.write(f"{state_name}")
            scoreboard += 1
            correct_guesses.append(answer_state)
        elif scoreboard == 50:
            writer_turtle.goto(0, 0)
            writer_turtle.write("Congratulations You guessed all 50/50 states")
            game_continue = False

# states to learn .csv
states_to_learn = [i for i in states_list if i in states_list and i not in correct_guesses]
data_dict ={
    "States Guessed": [correct_guesses],
    "States To Learn": [states_to_learn]
}
game_result = pandas.DataFrame(data_dict)
print(game_result)
game_result.to_csv("U.S States Game Result")
screen.exitonclick()
