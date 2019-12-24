import numpy as np

def sp():
    for i in range(3):
        print()


A = np.array([3,11,4,5])
B = np.array([5,0,3])
print(A)
print()
print(B)
sp()
# print(A+B) -> this doesn't work!

A = A[np.newaxis, :]
B = B[:, np.newaxis]
print(A)
print()
print(B)
sp()
# now broadcasting is possible!
print(A-B)

# 'None' can be used instead 'np.newaxis
