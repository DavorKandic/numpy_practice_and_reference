import numpy as np

def space():
    print()
    print('#' * 30)
    print()

    
# Changing type of elements with dtype parametar e.g. from ints to floats
array_a = np.array([[1,2,3],[4,5,6]], dtype=float)
print(array_a)

space()
# Creating arrays of zeros
array_z = np.zeros((3,3)) # 3x3 matrix of zeros
print(array_z)

space()
# Creating arrays of ones
array_ones = np.ones((3,3)) # 3x3 matrix of zeros
print(array_ones)

space()
# Creating arrays of any value
array_b = np.full((3,3), 5)
print(array_b)

space()
# Creating array of random values
array_rnd = np.random.random((3,4)) # 3x4 matrix of random values
print(array_rnd)

space()
# Creating array of random values
array_rndint = np.random.randint((3,4)) # 3x4 matrix of random values
print(array_rndint)
