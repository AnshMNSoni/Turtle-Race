# Turtle_Race:

import turtle as t
from random import *
from rich.console import Console

def clrall():
    console = Console()
    console.clear()

ss = t.Screen()
    
t1 = t.Turtle()
t2 = t.Turtle()
t3 = t.Turtle()
t4 = t.Turtle()
t5 = t.Turtle()
t6 = t.Turtle()
t7 = t.Turtle()

tt = [t1, t2, t3, t4, t5, t6, t7]
clr = ['red', 'blue', 'yellow', 'purple', 'green', 'orange', 'black']

ss.setup(width=1000, height=800)
y = -300
for obj in range(7):
    tt[obj].color(clr[obj])
    tt[obj].shape('turtle')
    
    tt[obj].penup()
    tt[obj].goto(-450, y)
    tt[obj].pendown()
    
    y += 100

user = ss.textinput('Who Will Win?', 'Enter Turtle color')

if (user == ''):
    ss.clear()
    clrall()
    print(f"Run Again to play the Game.")
    ss.exitonclick()
      
while True:
    for run in range(7):
        tt[run].penup()
        tt[run].fd(randint(10, 30))
        
        x = tt[run].xcor()
        
        if (x >= 480):
            if (user == clr[run]):
                clrall()
                print(f"Yes!, the {clr[run]} Turtle is the Winner.")
                ss.exitonclick()
                
            else:
                clrall()
                print(f"Sorry!, the {clr[run]} Turtle is the Winner.")
                ss.exitonclick()