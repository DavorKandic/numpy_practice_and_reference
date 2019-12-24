import numpy as np

def space():
    print()
    print('#' * 30)
    print()


# Both arrays have the same shape -> (2,2)!
array_a = np.array([[1,2],[3,4]])
array_b = np.array([[2,2],[6,6]])

# single array operations

# 1) sum
print(array_a.sum())  # same as sum() in python

space()

# suming with axis parametar

# a) summing by columns -> axis=0
print(array_a.sum(axis=0))  # 4 6

space()
# b) summing by rows -> axis=1
print(array_a.sum(axis=1))  # 3 7

space()
# 2) cumulative sum
print(array_a.cumsum())   # 1 3 6 10

space()
# 3) product
print(array_a.prod()) # 24

space()
# 4) cumulative product
print(array_a.cumprod())   # 1 2 6 24

space()
# two arrays math

# 1) addition
print(array_a + array_b)

space()
# 2) subtraction
print(array_a - array_b)

space()
# 3) multiplication
print(array_a * array_b)

space()
# 4) division
print(array_a / array_b)

space()
# 5) vector product a.k.a "dot product"
print(np.dot(array_a, array_b))

