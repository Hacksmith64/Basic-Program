def person(Name,Age=20):
    print(Name)
    print(Age)
person("White Devil",18)
person(18,"White Devil")

def sum(a,*b):
    c = a
    for i in b:
        c = c+i
    print(c)

sum(5,6,7,8,9)

def trail(*b):
    c = 0
    for i in b:
        c = c*i
    print(c)

trail(5,6,7,8,9)