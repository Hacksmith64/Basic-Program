from array import *

vals = array("i",[5,9,-8,2])
vals.reverse()
print(vals)
print(vals[1])
print(vals.buffer_info())
print(vals.typecode)
print(vals.remove(9))

value = array("i",[5,8,-8,2,6])
for i in range(len(value)):
    print(value[i])

values = array("i",[5,8,-8,2,6])
Newadd = array(values.typecode, (a*a for a in values))
for a in Newadd:
    print(a)
