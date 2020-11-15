class Students:
    School = "Venus"
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def Average(self):
        return (self.m1 + self.m2 + self.m3)/3
    def Get_m1(self):
        return self.m1
    def Set_m1(self,Values):
        self.m1 = Values
        return self.m1

    @classmethod
    def Get_School(cls):
        return cls.School
    @staticmethod
    def info():
        print("This is Student Class.. . is abc module")

s1 = Students(34,45,32)
s2 = Students(21,50,42)

print(s1.Get_m1())
print(s1.Set_m1(20))

print(s1.Average())
print(s2.Average())

print(Students.Get_School())
Students.info()