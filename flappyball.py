import pgzrun
HEIGHT=800
WIDTH=800
TITLE="flappy ball"
class Ball():
    def __init__(self,c,d,x,y):
        self.color=c
        self.diameter=d
        self.circlex=x
        self.circley=y
        self.vx=20
        self.vy=0
    def drawball(self):
        screen.draw.filled_circle((self.circlex,self.circley),self.diameter,self.color)

Ball1=Ball("blue",40,400,250)

def draw():
    screen.fill("black")
    Ball1.drawball()

pgzrun.go()

