import pgzrun
HEIGHT=500
WIDTH=600
p=Actor('ironman',(100,100))

speed=4
def draw():
    screen.fill('black')
    screen.clear()
    p.draw()

def update():
    player()

def player():
    if keyboard.UP and not p.top<0==p.colliderect():
        p.y-=speed  
        keyboard.DOWN==HEIGHT
           #p.collierect(DOWN) and not p.bottom>HEIGHT 
        p.y-=speed       
    #elif keyboard.DOWN and not p.bottom>HEIGHT:
     #   p.y+=speed 
        
       
pgzrun.go()          