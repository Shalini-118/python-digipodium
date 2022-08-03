from turtle import*
c=[(-300,300),(0,300),(300,300),(-150,150),(150,150),(0,0)]

for i in range(6):
    penup()
    goto(c[i])
    pendown()
    dot(45)
    pendown()
mainloop()    