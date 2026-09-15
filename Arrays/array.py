# Python program to demonstrate

from array import *
val = array('i', [1, 2, 3, 4, 5, 6])

print(val)
"""
for i in range(0,6):
    print(val[i], end = " ")

print("\n")
for x in val:
    print(x, end = ", ")
"""
val.insert(1,50)
print(val) # insert 50 at index 1
val.append(100)
print(val) # append 100 at the end
val[2] = 200
print(val) # change value at index 2 to 200

copyArray = array(val.typecode, (x for x in val))