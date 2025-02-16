class Car():
    def __init__(self,c,b,s,m):
        self.color=c
        self.brand=b
        self.seats=s
        self.model=m
    def display(self):
        print(self.color)
        print(self.brand)
        print(self.seats)
        print(self.model)
Car1=Car("red","jaguar",4,"sedan")
Car1.display()