import numpy as np

def space():
    print()
    print('#' * 30)
    print()

row_1 = [1,2,3,4,5]
row_2 = [6,7,8,9,10]
row_3 = [11,12,13,14,15]
row_4 = [16,17,18,19,20]
row_5 = [21,22,23,24,25]

test_data = np.array([row_1,row_2,row_3,row_4,row_5])
print(test_data)

space()
# Using slice for indexing
# Task: extract every 3rd and 4th value from every row
print(test_data[:,2:4:1]) # Remember! -> 1) : for every row,
                          #              2) start:end:step (default: step=1)

space()
# Task: extract every 3rd and 4th value from every row in reverse order
# e.g. -> 4th, 3rd
# Hint: use negative indexing
print(test_data[:,-2:-4:-1])

space()
# using booleans for indexing
greater_than_five = test_data > 5
print(greater_than_five)   # creates new matrix with True or False values
                           # according to condition

space()
# now, we will use our new boolean matrix to filter the original matrix
print(test_data[greater_than_five])

space()
# where:                    1)condition      if true    else(if false)
drop_under_5_array = np.where(test_data > 5, test_data, 0)
                            # so, it's basically ternary operator syntax
print(drop_under_5_array)

 
space()
# logical_and                            first condition, second condition
drop_under_5_and_over_20 = np.logical_and(test_data>5, test_data<20)
print(drop_under_5_and_over_20)  # creates boolean matrix

space()
# filtering original matrix via boolean matrix
print(test_data[drop_under_5_and_over_20])

