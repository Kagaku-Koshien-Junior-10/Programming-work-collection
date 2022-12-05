import numpy as np
def gr(N):
    a = 1.0
    b = np.sqrt(2) /2
    t = 1 / 4
    p = 1

    for i in range(N):
        an = (a + b) / 2
        bn = np.sqrt(a * b)
        tn = t - p * (a - an)**2
        pn = 2 * p

        a = an
        b = bn
        t = tn
        p = pn

    pi = (a + b)**2 / (4 * t)
    return pi
print(str(gr(3)))
