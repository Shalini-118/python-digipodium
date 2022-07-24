from turtle import *
speed('fastest')
pencolor('pink')
bgcolor('black')
pensize(10)
side=12
size=50
fillcolor('yellow')
begin_fill()
for i in range(side):
    fd(size)
    lt(360/side)
end_fill()
mainloop()    



