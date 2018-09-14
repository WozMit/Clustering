from sklearn import datasets;

iris = datasets.load_breast_cancer();
data = iris.data;
target = iris.target;
n, d, k = len(target), len(data[0]), len(set(target));
print(n, d, k);
for i in range(n):
	for j in range(d):
		print(data[i][j], "", end="");
	print(target[i]);