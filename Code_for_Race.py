# Turtle_Race:
from tkinter import messagebox
import turtle as t
from random import *

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
    messagebox.showwarning(title="Warning!", message="Empty Space found!")
    ss.exitonclick()
      
while True:
    for run in range(7):
        tt[run].penup()
        tt[run].fd(randint(10, 30))
        
        x = tt[run].xcor()
        
        if (x >= 480):
            if (user == clr[run]):
                messagebox.showinfo(title="Yes! Correct", message=f"Winner: {clr[run].upper()} Turtle")
                ss.exitonclick()
                
            else:
                messagebox.showinfo(title="Better Luch Next Time!", message=f"Winner: {clr[run].upper()} Turtle")
                ss.exitonclick()