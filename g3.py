import pgzrun
from random import randint

HEIGHT=500
WIDTH=600

music.play('bgm')

p=Actor('ironman',(100,100))
c=Actor('cookie')
c.x=randint(64,WIDTH-64)
c.y=randint(64,HEIGHT-64)
speed=3
score=0
def draw():
    screen.fill('black')
    screen.clear()# if not used image flash will appear.
    p.draw()
    c.draw()
    screen.draw.text(f'score:{score}',(WIDTH-80,10))

def update():
    player_control()
    update_score()

def update_score():
    global score
    if p.colliderect(c):
        score+=1
        c.pos=(randint(64,WIDTH-64),randint(64,HEIGHT-64))
        sounds.eating2.play()

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