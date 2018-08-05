import numpy as np;

# The Rosenbrock function
def Rosen(x):
	return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0);

x0 = np.array([2, 2, 5, 5]);
print(Rosen(x0));