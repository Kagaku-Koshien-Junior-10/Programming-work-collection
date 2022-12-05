import numpy as np
def main (N):
    sum=0.0
    for n in range (N):
        a = 1 / (np.math.factorial (n))
        sum = sum + a
    e = sum
    return e
print(main(100))
