num = 2.5
print(type(num))
num = 5
print(type(num))
num = 6+9j
print(type(num))
a = 5.6
b = int(a)
print(type(b))
k = b
print(k)
k = float(b)
print(k)
k = 6
c = complex(b,k)
print(c)
print(b<k)
print(bool(b<k))
bool = b<k
print(bool)
print(type(bool))
print(b>k)
print(int(True))
print(int(False))
List = [25,36,45,12]
print(type(List))
Sequence = {25,45,89,56}
print(type(Sequence))
Tuple = (25,45,89,56)
print(type(Tuple))
String = "Jayaram"
print(type(String))
St = 'a'
print(type(St))
print(range(10))
print(list(range(10)))
print(list(range(3,12,2)))
print(type(list(range(3,12,2))))
print(type((range(10))))
Dictionary = ("Jayaram","Redmi","Rahul","Iphone","Kiran","Oneplus")
print(Dictionary)
Dictionary = {"Jayaram":"Redmi","Rahul":"Iphone","Kiran":"Oneplus"}
print(Dictionary)
print(Dictionary.keys())
print(Dictionary.values())
print(Dictionary['Jayaram'])
print(Dictionary.get('Kiran'))
