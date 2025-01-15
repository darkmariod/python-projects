class People:
    classname = "people"

    def __init__(self, name: str):
        self.name = name
    
    def hi(self):
        print("Hola " + self.name)

mario = People("Mario")

mario.hi()

print(mario.classname)
print(people.classname)