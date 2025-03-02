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

ball1=Ball("blue",40,400,250)
GRAVITY=300
def draw():
    screen.fill("black")
    ball1.drawball()
def update(dt):
    uy=ball1.vy
    ball1.vy+= GRAVITY*dt
    ball1.circley+=(uy+ball1.vy)*0.5*dt

    ball1.circlex+=ball1.vx*dt

    if ball1.circley >= 760:
        ball1.vy=ball1.vy*-1

    if ball1.circlex >= 760:
        ball1.vx=ball1.vx*-1
    if ball1.circlex <= 40:
        ball1.vx=ball1.vx*-1


pgzrun.go()

