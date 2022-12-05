import numpy as np
def main(n,x):
	e = 1 + x
	for i in range(2,n+1):
		e = e + (x ** i) / np.math.factorial(i)
	return e
print(main(1000,1))
