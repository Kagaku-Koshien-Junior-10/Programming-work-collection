import numpy as np
def main(N):
    sum = 0.0
    for n in range (N):
        a = (np.math.factorial(4 * n))*(((26390 * n)) + 1103)
        b = ((np.math.factorial(n))**4) * (396 ** (4 * n))
        c = (2 * np.sqrt(2)) / (99**2)
        sum = sum + (a / b) * c
    pi = 1 / sum
    return pi
print(main(5))