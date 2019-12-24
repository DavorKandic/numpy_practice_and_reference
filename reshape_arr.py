import numpy as np

def space():
    for i in range(3):
        print()

foo = np.arange(start=1, stop=9)
print(foo)

space()

# syntax no.1
bar = foo.reshape((2,4))
print(bar)

space()

# syntax no.2
spam = np.reshape(a=foo, newshape=(2,4))
print(spam)

space()

# reorder last axis first
eggs = bar.reshape((4,2), order = 'C') # C-style (default) -> by rows
print(eggs)

space()

eggs = bar.reshape((4,2), order = 'F') # Fortran-style -> by columns
print(eggs)

space()

# classic matrix transpose
print(bar.T)

space()

# or
print(np.transpose(bar))

space()

# reshape into 3d
print(bar.reshape((2,2,2)))
