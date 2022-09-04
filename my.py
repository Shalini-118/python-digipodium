import random

WIDTH = 600
HEIGHT = 800
MAX_BULLETS = 3
ps=3
es=1
level = 1
lives = 3
score = 0

background = Actor('color',(100,100))
p = Actor('ironman', (200, 580))
e = Actor('zombie',(100,100))
bullets = []
bombs = []
def draw():
    screen.clear()
    background.draw()
    p.draw()
    for enemy in enemies:
        enemy.draw()
    for bullet in bullets:
        bullet.draw()
    for bomb in bombs:
        bomb.draw()
    draw_text()
def update(delta):
    move_player()
    move_bullets()
    move_enemies()
    create_bombs()
    move_bombs()
    check_for_end_of_level()    
def move_player():
    if keyboard.RIGHT and not p.right>WIDTH:
        p.x+=ps
        p.angle=-10
    elif keyboard.LEFT and not p.left<0:
        p.x+=-ps
        p.angle=10
    elif keyboard.DOWN and not p.bottom>HEIGHT:
        p.y+=ps
    elif keyboard.UP and not p.top<0:
        p.y+=-ps
    else:
        p.angle=0        

def move_enemies():
    if p.x>e.x:
        e.x+=es
    if p.x<e.x:
        e.x+=-es
    if p.y>e.y:
        e.y+=es
    if p.y<e.y:
        e.y+=-es
    if p.colliderect(e)

def move_bullets():
    pass

def create_bombs():
    pass

def move_bombs():
    pass

def check_for_end_of_level():
    pass

def draw_text():
    pass    