import turtle as t
import pandas as pd

screen=t.Screen()
screen.setup(725,491)
screen.title("quiz States U.S game")
image="blank_states_img.gif"
screen.addshape(image)
t.shape(image)


data=pd.read_csv("50_states.csv")
state_list=data.state.to_list()
print(state_list)

        
guessed_states=[]



while len(guessed_states)<50:
    user_answer=t.textinput(f"Guess the state {len(guessed_states)}/50", "Please enter a State name").title()
    if user_answer in state_list:
        guessed_states.append(user_answer)
        name=t.Turtle()
        name.hideturtle()
        name.penup()
        state_data=data[data.state==user_answer]
        name.goto(state_data.x.item(), state_data.y.item())
        name.write(state_data.state.item())
if not len(guessed_states)<50:
    result=t.Turtle()
    result.hideturtle()
    result.penup()
    result.goto(-100,0)
    result.write("You Win!",font=("Arial",30))
screen.exitonclick()