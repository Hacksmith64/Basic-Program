import string
Values = input("""Enter the String""")
print("The Original String is ;"+Values)
res = sum([i.strip(string.punctuation).isalpha() for i in Values.split()])
print(Values)
print("number of"+str(res))