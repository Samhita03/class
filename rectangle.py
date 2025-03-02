import pgzrun
HEIGHT=800
WIDTH=800
TITLE="rectangle"
class Rectangle():
    def __init__(self,c,l,b,x,y):
        self.color=c
        self.length=l
        self.breadth=b
        self.recx=x
        self.recy=y
        self.vx=20
        self.vy=0
        self.rect=Rect((self.recx,self.recy),(self.length,self.breadth))
    def drawrec(self):
        screen.draw.filled_rect(self.rect,self.color)

rec1=Rectangle("blue",400,250,60,50,)

def draw():
    screen.fill("black")
    rec1.drawrec()
def update():
    pass

pgzrun.go()

