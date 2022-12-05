import numpy as np
def X(N):
    sum = 0.0
    for i in range (N):
        a = ((-1)**i) * np.math.factorial(6 * i) * (13591409 + 545140134 * i)
        b = (np.math.factorial(3 * i) * np.math.factorial(i) ** 3) * (640320 ** 3) ** (i + 1/2)
        sum = sum + ( a / b ) * 12
    pi = 1 / sum
    return pi
print(str(X(2)))
