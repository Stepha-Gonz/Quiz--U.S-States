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

        
guessed_states=[]



while len(guessed_states)<50:
    user_answer=t.textinput(f"Guess the state {len(guessed_states)}/50", "Please enter a State name, or 'exit' to leave the game").title()
    if user_answer=="Exit":
        not_guessed_states=[state for state in state_list if state not in guessed_states]
        missing_states_data=pd.DataFrame(not_guessed_states)
        missing_states_data.to_csv("states_to_learn.csv")  
        break
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
    


