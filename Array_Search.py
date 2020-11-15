from array import *

arr = array("i",[])
n = int(input("Enter the Lenght of the Array"))
for i in range(n):
    x = int(input("Enter the next Value"))
    arr.append(x)
print(arr)

Val = int(input("Enter the Value for Search"))
k = 0
for e in arr:
    if e == Val:
        print(k)
        break
    k+=1
print(arr.index(Val))
