import turtle
import pandas

screen=turtle.Screen()
screen.title('US States Game')

# adding image
image='./blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data=pandas.read_csv('./50_states.csv')

guessed_states=[]

while len(guessed_states)<50:
    answer_state=screen.textinput(title=f'{len(guessed_states)}/50 States Correct', prompt="What's another state name?")
    answer_state=answer_state.title()

    all_states=data.state.to_list()

    if answer_state=='Exit':
        break

    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # gives the column of the state where it matches the answer_state
        state_data=data[data.state==answer_state]
        x_cor=int(state_data['x'])
        y_cor=int(state_data['y'])
        # or x_cor=state_data.x and state_data.y
        t.goto(x_cor, y_cor)
        t.write(arg=answer_state, align='center')
        guessed_states.append(answer_state)

print("The states that you were unable to name were: ")
for i in range(50):
     if all_states[i] not in guessed_states:
        print(all_states[i])

