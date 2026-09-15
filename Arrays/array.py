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

val.pop(3) # remove value at index 3
print(val) # print array after removing value at index 3
val.pop() # remove last value
print(val) # print array after removing last value
val.remove(50) # remove first occurrence of 50
print(val) # print array after removing first occurrence of 50