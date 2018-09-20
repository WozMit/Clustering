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
#plot(p);
print("Mean:");
c = np.mean(p, axis=0);
print(c);
print(J(c), "\n");
#plt.plot(c[0], c[1], 'go');
res = minimize(J, c, method='BFGS', options={'disp': True});
c = res.x;
#plt.plot(c[0], c[1], 'ro');
print("\nSolution found:");
print(c);
#plt.show();

# Second method
print("\n\nSecond method");
c = np.mean(p, axis=0);
print(c);
print(J(c));
for _ in range(20):
	num, den = 0, 0;
	for pi in p:
		norm = np.sqrt(np.sum([d*d for d in pi-c]));
		num += pi / norm;
		den += 1 / norm;
	c = num / den;
	print(c);
	print(J(c));