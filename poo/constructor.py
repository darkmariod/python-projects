class People:
    def __init__(self, name):
        self.name = name

    def hi(self):
        print("hello" + self.name) 

mario = People("mario")

mario.hi()