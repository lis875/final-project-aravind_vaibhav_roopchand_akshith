from turtle import *
from story import *
from hangman import *
import time

screen = Screen()
screen.setup(width=1.0, height=1.0)

intro = {}
def get_user_input(title, prompt):
    penup()
    hideturtle()
    setpos(-100, 200)
    write(title, font=('Arial', 20))
    user_input = textinput(title, prompt)
    clear()
    return user_input

intro['detective1'] = get_user_input("Detective 1", detective1)
intro['detective2'] = get_user_input("Detective 2", detective2)
intro['user_color'] = get_user_input("Color", color_prompt)
intro['user_movie'] = get_user_input("Movie", movie_promt)

def print_on_turtle(para):
    penup()
    hideturtle()
    write(para, font=('Arial', 15))

def substitute_paragraph(paragraph: str):
    for item, value in intro.items():
        paragraph = paragraph.replace(item, value)
    return paragraph

if __name__=="__main__":
    while True:
        para = str(para1)
        para = substitute_paragraph(para)
        setpos(-500, 0)
        print_on_turtle(para)
        accept_mission_answer = textinput("Name", accept_mission)
        if accept_mission_answer == "2":
            pass
            # Stays in jail
            # Do you want to restart
            # if restart -> continue
            # if quit -> quit turtle
        if accept_mission_answer == "1":
            break
    
    # print_on_turtle(hangman_hint)
    # hangman module
    answer = 'wrong'
    while answer != 'correct':
        hangman_output = hangman()
        print(hangman_output)
        if hangman_output == 'fail':
            pass
            pin = get_pin()
            print_on_turtle(f"THE PIN IS - {pin}")
            time.sleep(5)
            clear()
        if hangman_output == 'pass':
            answer = 'correct'
    color('black')
    penup()
    clear()
    para = str(para2)
    para = substitute_paragraph(para)
    setpos(-500, 0)
    print_on_turtle(para)
    continue_with_story = textinput("Continue", "Type anything to continue")
    clear()
    para = str(para3)
    para = substitute_paragraph(para)
    setpos(-500, 0)
    print_on_turtle(para)
    continue_with_story = textinput("Continue", "Type anything to continue")
    clear()
    para = str(para4)
    para = substitute_paragraph(para)
    setpos(-500, 0)
    print_on_turtle(para)
    mission = textinput("Choose a Mission", "Choose mission \n 1. PLANE HIJACK \n 2. BANK ROBBERY")
    print(mission)
    if mission == "2":
        clear()
        setpos(-500, 0)
        print_on_turtle("Unfortunately the bank is closed today. Go hijack the plane\n")
    print_on_turtle("\nLet's Hijack the plane")
    setpos(-500, -100)
    para = str(para5)
    para = substitute_paragraph(para)
    print_on_turtle(para)
    is_gun_valid = False
    while is_gun_valid != True:
        gun = textinput("Choose a Gun", "Choose a gun \n1) AK47 \n2) Desert Eagle \n3) Invisible rocket launcher")
        clear()
        if gun == '1':
            para = str(para6)
            para = substitute_paragraph(para)
            setpos(-500, 0)
            print_on_turtle(para)
            print_on_turtle("Turns out AK47 is too huge to handle with the security. Try something else")
        else:
            is_gun_valid = True
    if gun == '3':
        gun = "Invisible rocket launcher"
        clear()
        para = str(para7)
        para = substitute_paragraph(para)
        setpos(-500, 0)
        print_on_turtle(para)
        rob_bank = textinput('Rob the bank', "Do you want to rob a bank? \n1. Yes \n2. No")
        clear()
        if rob_bank == '1':
            setpos(-500, 0)
            print_on_turtle(para80)
        if rob_bank == '2':
            setpos(-500, 0)
            print_on_turtle(para81)

    if gun == '2':
        gun = "Desert Eagle"
        clear()
        para = str(para9)
        para = substitute_paragraph(para)
        setpos(-500, 0)
        print_on_turtle(para)
        continue_with_story = textinput("Continue", "Type anything to continue")
        clear()
        para = str(para10)
        para = substitute_paragraph(para)
        setpos(-500, 0)
        print_on_turtle(para)


    done()
    