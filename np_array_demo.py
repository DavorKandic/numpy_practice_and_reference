import numpy as np

# Numpy array has a homogenous data type -> all elements are ints, floats, strings ...

array_a = np.array([1,2,3,4,5]) # we must pass ONE argument to np.array
print(array_a)
print(array_a.shape) # (5,) -> first value represents rows, second columns
                     # so first value is 1, but it is not explicitly stated!
print()

array_b = np.array([[1,2,3,4,5],[1,2,3,4,5]])  # just ONE argument, remember!
print(array_b)
print(array_b.shape) #(2,5) -> 2 rows, 5 columns

print()
# Let's see what is happening if we pass heterogenous list as np.array argument
array_c = np.array([1,2,3,4,5, "davor"])
print(array_c)   # hint: np.array converted all values to strings!

array_d = np.array([1,2,3,4,5, 3.14])
print(array_d)  # all ints are converted to floats


array_e = np.array(["some string", 7.2, True, 34])
print(array_e) # all values are converted to strings

array_f = np.array([True, False, True, 42])
print(array_f) # booleans converted to ints: True => 1, False => 0


# create array with shape (5,2) in one line



