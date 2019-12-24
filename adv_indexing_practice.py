import numpy as np

def space():
    print()
    print('#' * 30)
    print()

# create array with arange(start,end,step) method
array_a = np.arange(0,100,5)
print(array_a)
print(array_a.size)

space()
# reshaping array with reshape(rows, columns) method
array_a_reshape = array_a.reshape(4,5) # 4 rows, 5 columns
print(array_a_reshape)

space()
# neg indexing
# Task: get last element(column) in every row
print(array_a_reshape[:,-1])

space()
# let's revise matrix transposition
array_a_reshape_t = array_a_reshape.T
print(array_a_reshape_t)

space()
# boolean indexing, all on same line!
# So with condition we are creating boolean matrix and than use it to filter
array_a_above_50 = array_a_reshape[array_a_reshape > 50]
print(array_a_above_50)

space()
# python slice
print(array_a_above_50[0:len(array_a_above_50):2])

space()
# slice of (every) row
print(array_a_reshape[:, 0:5:2])

space()
# another example using where(condition, True, False)
print(np.where(array_a_reshape>50, array_a_reshape, -1))

space()
# same, but multiply all values by 2
print(np.where(array_a_reshape>50, array_a_reshape*2, -1))
