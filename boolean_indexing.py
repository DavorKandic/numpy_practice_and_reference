import numpy as np

def sp():
    for i in range(3):
        print()


# Suppose that we have numpy array 'foo' and that we want
# to turn all threes to zeros

foo = np.array([
    [3,9,7],
    [2,0,3],
    [3,3,1]
    ])

print(foo)

sp()

# creating of 'mask'(boolean matrix)
mask = (foo == 3)
print(mask)

sp()

# filtering original array 'foo' via 'mask' and setting True values to zero
foo[mask] = 0
print(foo)

sp()

# Another example

rows_1_and_3 = np.array([True, False, True])
cols_2_and_3 = np.array([False, True, True])

# return rows 1 and 3
print(foo[rows_1_and_3])

sp()

# return columns 2 and 3
print(foo[:, cols_2_and_3])

