class Student():
    def __init__(self,n,a,t,s):
        self.name=n
        self.age=a
        self.teacher=t
        self.school=s
    def display(self):
        print(self.name)
        print(self.age)
        print(self.teacher)
        print(self.school)
student1=Student("david",10,"bob","abc")
student1.display()