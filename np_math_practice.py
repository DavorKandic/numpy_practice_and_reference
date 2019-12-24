import numpy as np

def space():
    print()
    print('#' * 30)
    print()

array_a = np.array([[1,2,3],[4,5,6],[7,8,9]])
array_b = np.array([[2,2,2],[3,4,5],[6,7,8]])
print(array_a)
print(array_b)


space()
# sum of columns
print(array_a.sum(axis=0))

space()
# sum of rows
print(array_a.sum(axis=1))

space()
# peak-to-peak -> (max - min) of every row 
print(array_a.ptp(axis=1))    # 2 2 2

space()
# peak-to-peak -> (max - min) of every column 
print(array_a.ptp(axis=0))    # 6 6 6

space()
# peak-to-peak -> (max - min) of entire array! (without axis) 
print(array_a.ptp())    # 8

space()
# min, max, mean of whole array (of course, we can also use axis!)
print(array_a.min())    # 1
print(array_a.max())    # 9
print(array_a.mean())   # 5.0

space()
# multi-array operations
# power
print(np.power(array_a, array_b))

space()
# creating third array
array_c = np.array([[1,1,1],[2,2,2],[3,3,3]])
# addition of three arrays
print(array_a + array_b + array_c)
