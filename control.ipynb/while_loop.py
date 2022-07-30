'''start=100
while start>0:
 print("start:",start)
   start-=10'''
from turtle import*
value=300
while value>0:
    fd(value)
    left(90)
    value-=10
    write(value)   
mainloop()    