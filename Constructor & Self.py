class Computer:
    def __init__(self):
        self.name = "White Devil"
        self.age = 18

    def compare(self,Others):
        if self.age == Others.age:
            return True
        else:
            return False

c1 = Computer()
c1.age = 30
c2 = Computer()
print(id(c1))
print(id(c2))
if c1.compare(c2):
    print("There are Same")
else:
    print("There are Different")
c1.name = "Jayaram"
c1.age = 17


print(c1.name)
print(c2.name)

print(c1.age)
print(c2.age)

