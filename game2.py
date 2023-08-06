import pgzrun
from random import randint

#screen size
WIDTH=1000
HEIGHT=500


#objects

p=Actor('hero')
e=Actor('enemy')
c=Actor('fruit')

#configs
c.x=randints (50,WIDTH-50)
c.y=randint(50,HEIGHT-50)
p.pos=(WIDTH/2,HEIGHT/2)
e.pos=(-100,HEIGHT/2)


#drawing on screenr
def draw():
 screen.clear()
 p.draw()
 e.draw()
 c.draw()
def update(dt):
   #player control
   if keybord.left:
     p.x -=5
    if keybord.right:
     p.x +=5
    if keybord.up:
     p.y +5=ps 
    if keybord.down:
     p.y -=space

 print(dt)
#game loop
pgzrun.go()   