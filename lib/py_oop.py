class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def myMethod(self):
        print("Hello " + self.name)

    def myMethod2(self, level):
        print(level)

p1 = Person('leo', 25)

print(p1.name)
print(p1.age)
p1.myMethod()
p1.myMethod2(3)
