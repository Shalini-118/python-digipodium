from turtle import*

speed('fastest')

for i in range(4):
    pencolor('red')
    fd(100)
    
    
    for i in range(6):
        pencolor('blue')
        pensize(3)
        fd(100)
       # write(i, font=('arial',14,'normal'),align='left')
        lt(360/6)
    lt(360/4) 
mainloop()       
