import numpy as np;

# Read the data
ever = np.load('mnist.npz');
data = ever['arr_0'];
target_p = ever['arr_1'];
target = np.zeros(70000);
for i in range(70000):
	for j in range(10):
		if(target_p[i][j] == 1):
			target[i] = j;
print("70000 784 10");
for i in range(70000):
	for j in range(784):
		print(int(data[i][j] * 255), "", end="");
	print(int(target[i]));