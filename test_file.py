import numpy as np;
import matplotlib.pyplot as plt;

d = [];
for _ in range(20495):
  a, b = map(float, input().split(' '));
  d.append([a, b])
data = np.array(d);

x = data[:, 0];
y = data[:, 1];

plt.ylim((75, 200));
plt.xlim((75, 200));

#plt.plot(x, y, 'b.');

#plt.show();

data.sort();
print(data[-10:]);