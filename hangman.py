from turtle import *
from config import *
from story import *



def get_pin():
	return str(int(JAIL_CELL) + int(NUMBER_OF_DAYS_IN_JAIL))
	
def go_to(x, y, p):
	hideturtle()
	penup()
	goto(x,y)
	setheading(p)
	pendown()
	
def hang(stage):
	speed(0)
	if stage[0]==0:
		go_to(50,0,0)
		forward(600)
		go_to(100,0, 90)
		forward(200)
		right(90)
		forward(100)
		right(90)
		forward(25)
	elif stage[0]==1:
		go_to(200, 150, 0)
		circle(12.5)
	elif stage[0]==2:
		go_to(200,150, -90)
		forward(50)
	elif stage[0]==3:
		go_to(200,140, -45)
		forward(25)
		go_to(200,140, -135)
		forward(25)
	elif stage[0]==4:
		go_to(200,100, -45)
		forward(25)
		go_to(200,100, -135)
		forward(25)
	stage[0]+=1
	return 0
	
def check_pin(jail_pin, stage):
	user_pin=textinput(f'JAIL PIN', hangman_input_prompt)
	if user_pin == jail_pin:
		return "pass"
	else:
		hang(stage)
		return "fail"

def hangman():
    stage=[0]
    setpos(100, 300)
    color("red")
    write(hangman_hint, font=('Arial', 20, "bold"))
    while True:
        jail_pin=get_pin()
        hangman_result = "fail"
        while hangman_result!="pass" and stage[0]<=4:
            hangman_result = check_pin(jail_pin, stage)
        return hangman_result
	
	
if __name__=="__main__":
	hangman_result = hangman()
	print(hangman_result)