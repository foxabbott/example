import numpy as np
print("Hello wordl")

a = (1 + (1 + 2))

x = np.array([1, 2, 3])
m = np.ones((3, 3))

y = np.dot(m, x)
print(y)

# A function which evluates a quadratic

def quadratic_formula(a, b, c):
    d = np.sqrt(b**2 - 4*a*c)
    x1 = (-b + d) / (2*a)
    x2 = (-b - d) / (2*a)
    return x1, x2

print("I'm just faffing on")