import numpy as np
def A(N):
    a = np.radians(360 / N)
    pi = N * np.sin(a) / 2
    return pi
print(str(A(10000)))
