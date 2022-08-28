import pgzrun

HEIGHT=500
WIDTH=600

p=Actor('ironman',(100,100))
speed=3

def draw():
    screen.clear()# if not used image flash will appear.
    p.draw()

def update():
    player_control()


def player_control():
    print('updating')
    if keyboard.RIGHT and not p.right>WIDTH:
        p.x+=speed
        p.angle=-10
    elif keyboard.LEFT and not p.left<0:
        p.x-=speed
        p.angle=10
    elif keyboard.UP and not p.top<0:
        p.y-=speed    
    elif keyboard.DOWN and not p.bottom>HEIGHT:
        p.y+=speed   
    else:
        p.angle=0 #to restore original position              
      

pgzrun.go()# outside the function    