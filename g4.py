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
    if keyboard.UP or keyboard.DOWN: 
        p.top<0 and not p.bottom>HEIGHT
        p.y-=speed    
    #if keyboard.DOWN and not p.bottom>HEIGHT:
      #  p.y+=speed   
    else:
        p.angle=0   
pgzrun.go()          