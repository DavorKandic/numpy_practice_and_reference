import numpy as np

def space():
    print()
    print('#' * 30)
    print()

array_a = np.array([[1,1,1,1],[2,2,2,2],[3,3,3,3]])
array_b = np.array([0,1,2,3])
array_c = np.array([[1],[2],[3]])

# The idea behind broadcasting is
# operations on array of different shape and size

# addition of two arrays of different shape and size
print(array_a + array_b)
