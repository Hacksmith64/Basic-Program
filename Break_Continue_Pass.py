#Break
av = 10
x = int(input("How many Candy do you You Want?"))
i = 1
while i <= x:
    if i>av:
        print("Out of Stock")
        break
    print("Candy")
    i+=1
print("Bye")
#Continue
for i in range(1,10):
    if i%3==0 or i%5 == 0:
        continue

    print(i)
print("Bye")
#Pass
for i in range(2,10):


    if i%2!=0:
        pass

    else:
        print(i)
print("Bye")