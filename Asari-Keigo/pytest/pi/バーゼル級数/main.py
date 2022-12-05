import numpy as np
def basel(N):
    x = np.arange(1, N + 1)
    pi = np.sqrt(6 * np.sum(1 / x**2))
    return pi
print(str(basel(10000)))
