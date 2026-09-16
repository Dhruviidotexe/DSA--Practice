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

#slicing of array:
abc = val[0 : 2] # slice array from index 0 to 2
print(abc) # print sliced array
# [::-1] reverse the array

# creating an array and inserting elements into the array
arr = array( 'i', [])
n = int(input("Enter the length of the array: "))

for i in range(n):
    arr.append(int(input("Enter the next value: ")))

for x in arr:
    print(x, end= " ")

# printing the index of an element:
arr= array('i', [1, 2, 3, 4, 5, 6])
i= arr.index(4) # get the index of 4
print("\nThe index of 4 is: ", i)

# alias- giving nicknames to the module name that we want to import and use in our file.

import numpy as np
np.array([1, 2, 3, 4, 5]) # creating an array using numpy

# if array is created using the numpy module, we do not need to write the typecode.
val = np.array([1, 2, 3, 4, 5])
for x in val:
    print(x, end = " ")

# linspace() function in numpy module is used to create an array with evenly spaced values over a specified range.
arr = np.linspace(1, 10, 5) # create an array with

# logspace
arr = np.logspace(1, 10, 5) # create an array with logarithmically spaced values

# arrange() function in numpy module is used to create an array with evenly spaced values over a specified range.
arr = np.arange(1, 10, 2) # create an array with values from 1 to 10 with a step of 2
