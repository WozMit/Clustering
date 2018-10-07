import numpy as np;
import matplotlib.pyplot as plt;

def J(x, c):
	return np.sum([np.abs(xi - c) for xi in x]);

np.random.seed(0);
x = np.array([np.random.randint(1, 20) for _ in range(21)]);
x = np.sort(x);
print(x);

a = np.arange(x[0], x[-1] + 1, 0.01);
b = np.array([J(x, ci) for ci in a]);

plt.plot(a, b);

plt.show();