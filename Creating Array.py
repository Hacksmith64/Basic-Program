from numpy import *
arr = array([1,2,3,4,5,6])
print(arr.dtype)
print(arr)

arr = array([1,2,3,4,5,6],float)
print(arr.dtype)
print(arr)

arr = linspace(0,15,16)
print(arr)

arr = arange(1,15,2)
print(arr)

arr = logspace(1,40,5)
print(arr)

arr = zeros(5)
print(arr)

arr = ones(5)
print(arr)

arr = ones(5,int)
print(arr)