import numpy as np;
import matplotlib.pyplot as plt;
from scipy.optimize import minimize;

def plot(p):
	for pi in p:
		plt.plot(pi[0], pi[1], 'bo');

def J(c):
	dist = 0;
	for pi in p:
		dist += np.sqrt(np.sum([d*d for d in pi-c]));
	return dist;

p = np.array([[1, 1], [4, 1], [1, 6], [-1, 4], [5, 4], [4, 25]]);
plot(p);
c = np.array([[0, 0]]);
print(J(c));
res = minimize(J, c, method='BFGS', options={'disp': True});
c = res.x;
plt.plot(c[0], c[1], 'ro');
print("Solution found:");
print(c);
print("\nMean:");
mean = np.mean(p, axis=0);
print(mean);
plt.plot(mean[0], mean[1], 'go');
plt.show();