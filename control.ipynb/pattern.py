from turtle import*
side=10
pensize(10)
speed(0)
for i in range(3):
    pencolor('pink')
    forward(100)

    for i in range(3):
        pencolor('red')
        forward(100)
        
        for i in range(3):
            pencolor('pink')
            forward(100)

        rt(45) 
    rt(45)       
mainloop()            