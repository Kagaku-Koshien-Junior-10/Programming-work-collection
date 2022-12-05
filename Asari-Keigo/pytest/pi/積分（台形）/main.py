import numpy as np
def B(N):
    x = np.arange(N + 1) / N
    y = np.sqrt(1 - x**2)
    z = (y[0:N] + y[1:N+1]) / 2
    pi = 4*np.sum(z) / N
    return pi
print(str(B(123456)))
