import numpy as np;
import matplotlib.pyplot as plt;

n, d, k = [int(x) for x in input().split(' ')];
data = np.zeros((n, d));
lbl = np.zeros(n);
markers = ['.', '+', '_', '1', '^', '+', 'x', '<', '|'];
gg = [0] * k;
for _ in range(n):
	x = [float(x) for x in input().split(' ')];
	gg[int(x[-1])] += 1;
print(gg);
print(sum(gg) == n);
#for i in range(n):
	#x, y, c = [float(x) for x in input().split(' ')];
	#plt.plot(x, y, markers[int(c)], color='black');
	#data[i] = x[:-1];
	#lbl[i] = x[-1];

#plt.ylim((-15, 16));
#plt.xlim((-12, 19));
#plt.plot(data, '.b');
#plt.title("Dataset sintético 4");
#plt.show();
#print(data);

"""d = [];
for _ in range(20495):
  a, b = map(float, input().split(' '));
  d.append([a, b])
data = np.array(d);

x = data[:, 0];
y = data[:, 1];

#plt.ylim((75, 200));
#plt.xlim((75, 200));

plt.plot(x, y, '.', c='black');

plt.show();

data.sort();
print(data[-10:]);"""