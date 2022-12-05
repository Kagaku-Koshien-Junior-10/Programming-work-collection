import numpy as np
def X(N):
    sum = 0.0
    for i in range (N):
        a = ((-1)**i) * np.math.factorial(4 * i) * (1123 + 21460 * i)
        b = (882**(2 * i + 1)) * ((4**i) * np.math.factorial(i))**4
        sum = sum + a / b
    pi = 4 / sum
    return pi
print(X(5))
