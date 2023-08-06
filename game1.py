from random import randint
import pgzrun

width=1000
height=500


class player (Actor):
    '''this is class player ,that inherits form actor'''
       speed=5




class Enemy(Actor):
    speed=5
    pos=(-100,HEIGHT/2)
    def enemy_tracking(self,p):
       #enemy tracks player
       if p.x>self.x:
          self





class Fruit(Actor):
    x=randint(50,width-50)
    y=randint(50,height-50)

    def recolate(self):
        if keybord.left:
         p.x -=5
        if keybord.right:
         p.x +=5
        if keybord.up:
         p.y +5=ps 
        if keybord.down:
         p.y -=ps 
        if keybord.space:
           p.angle+=ps 


#game code starts now
p=player ('Hero')
e=Enemy
