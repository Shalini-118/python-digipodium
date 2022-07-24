from turtle import *
speed('slowest')
pencolor('pink')
bgcolor('white')
pensize(10)
side=12
size=50
fillcolor('yellow')
begin_fill()
for i in range(size):
 fd(size)
 lt(360/side)
end_fill()
mainloop()    