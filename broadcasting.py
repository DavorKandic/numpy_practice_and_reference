import numpy as np

def sp():
    for i in range(3):
        print()

bart = np.array([
    [1,1,1],
    [2,2,2],
    [3,3,3],
    [4,4,4]
    ])

lisa = np.array([
    [5,3,10],
    [5,3,10],
    [5,3,10],
    [5,3,10]
    ])

kids = bart + lisa

print(kids)

lisa2 = np.array([5,3,10])

kids2 = bart + lisa2

sp()

print(kids2)

lisa3 = np.array([5,3,10,35])

bart2 = np.array([1,2,3,4])

kids3 = bart2.T + lisa3.T

sp()

print(kids3)
sp()
# using random.randint()
np.random.seed(1234)
A = np.random.randint(low = 1, high = 10, size = (3,4))
B = np.random.randint(low = 1, high = 10, size = (3,1))
print(A)
sp()
print(B)
sp()
print(A + B)

