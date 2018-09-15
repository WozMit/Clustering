import numpy as np;
import time as tm;
from scipy.spatial import distance;
from scipy.optimize import minimize, basinhopping;
import matplotlib.pyplot as plt;
from mpl_toolkits.mplot3d import Axes3D;
from sklearn.decomposition import PCA;
from sklearn import metrics;

def ShowIris(x, y, title):
	X = x[:, :2];
	fig = plt.figure(1, figsize=(8, 6));
	ax = Axes3D(fig, elev=-150, azim=110);
	X_reduced = PCA(n_components=3).fit_transform(data);
	ax.scatter(X_reduced[:, 0], X_reduced[:, 1], X_reduced[:, 2], c=y,
			cmap=plt.cm.Set1, edgecolor='k', s=40);
	ax.set_title(title);
	ax.set_xlabel("1st eigenvector");
	ax.w_xaxis.set_ticklabels([]);
	ax.set_ylabel("2nd eigenvector");
	ax.w_yaxis.set_ticklabels([]);
	ax.set_zlabel("3rd eigenvector");
	ax.w_zaxis.set_ticklabels([]);
	plt.show();

def GetClusters(centers):
	centers = centers.reshape((k, d));
	clusters = [[] for _ in range(k)];
	distances = [];
	for i in range(n):
		min_distance = distance.minkowski(data[i], centers[0], 2);
		idx = 0;
		for j in range(1, k):
			d_temp = distance.minkowski(data[i], centers[j], 2);
			if(d_temp < min_distance):
				min_distance = d_temp;
				idx = j;
		clusters[idx].append(i);
		distances.append(min_distance);
	return clusters, distances;


def J(centers):
	clusters, distances = GetClusters(centers);
	return np.mean(distances)**2;

start_time = tm.time();

# Read the data
n, d, k = map(int, input().split(" "));
data = np.zeros((n, d));
target = np.zeros(n);
for i in range(n):
	x = [float(x) for x in input().split(" ")];
	data[i] = x[:d];
	target[i] = x[d];
target = target.astype(int);

# Scale the data
data = (data - np.mean(data))/np.std(data);

# Choose initial centers
centers = np.zeros((k, d));
mini = np.amin(data, axis=0);
jump = (np.amax(data, axis=0) - mini) / (k + 1);
for i in range(k):
	centers[i] = mini + jump * (i + 1);
centers = centers.flatten();

# Optimize function
print("Initial function value:", J(centers));

res = minimize(J, centers, method='BFGS',
		options={'disp': True, 'maxiter': 10});
#res = basinhopping(J, centers, niter=2, disp=True);
centers = res.x;

print("Centers found:");
print(centers.reshape((k, d)));
clusters, distances = GetClusters(centers);
labels = np.zeros(n, dtype=int);
for i in range(len(clusters)):
	for p in clusters[i]:
		labels[p] = i;

#print("Labels:");
#print(labels);
print("\n");
#print("Accuracy: %.3f %%" %(100 * (sum(target == labels) / len(target))));
print("Adjusted mutual information: %.3f %%" %(100 * metrics.adjusted_mutual_info_score(target, labels)));

print("\nTotal time = "+str(tm.time()-start_time)+" s");

print("\nK-means:");
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=k, random_state=0).fit(data);
print("Adjusted mutual information: %.3f %%" %(100 * metrics.adjusted_mutual_info_score(target, kmeans.labels_)));

ShowIris(data, labels, "Global optimization algorithm");