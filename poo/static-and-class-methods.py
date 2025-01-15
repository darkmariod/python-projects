class People:
    classname = "people"

    def __init__(self, name: str):
        self.name = name
    
    def hi(self):
        print("Hello " + self.name)

    @staticmethod
    def helloworld(cls):
        print("Hello World")

    @classmethod
    def helloworld2():
        print("Hello World 2")

mario = People("Mario")

mario.hi()

mario.helloworld2()
People.helloworld2()