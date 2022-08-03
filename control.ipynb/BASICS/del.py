from tkinter import ARC
from turtle import *

from zmq import CURVE
pencolor('red')
pensize(10)
forward(100)# move forward 200 units
rt(90)# turns left 90 degrees
forward(200)
rt(90)
forward(100)
rt(90)
forward(200)
rt(25)
fd(110)
rt(125)
fd(115)
lt(60)
fd(300)
rt(90)
fd(200)
rt(90)
fd(300)
penup()
goto(50,40)
pendown()
dot(30)
penup()
goto(50,100)
pendown()
lt(180)
fd(300)
rt(60)
fd(110)
penup()
goto(500,-50)
pendown()



mainloop()