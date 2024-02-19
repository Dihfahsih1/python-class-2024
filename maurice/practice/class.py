class Students:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def intro(self):
        print(f'Name: {self.name},Age: {self.age}')
s1=Students("maurice",20)
s1.intro()
