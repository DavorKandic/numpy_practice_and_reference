import numpy as np

def space():
    print()
    print('#' * 30)
    print()

array_a = np.array([[1,2,3],[4,5,6]])
print(array_a.shape)
print(array_a.size)   # => 6 (rows x cols)

space()
# Reshaping array => arguments have to be numbers whos product is size of array
array_b = array_a.reshape(3,2)
print(array_b)

space()

array_c = array_b.reshape(6,1)
print(array_c)

space()
# Transposing np.array => invert rows and columns
print(array_a)
array_t = array_a.T
print(array_t)

space()
# Indexing in np.array
print(array_t[0])     # first row
print(array_t[:,1])   # second element in every row a.k.a second column
print(array_t[0,0])   # first element in first row
