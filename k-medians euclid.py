import numpy as np;
import time as tm;
from scipy.spatial.distance import minkowski;
from sklearn import metrics;

def GetClusters(centers):
	centers = centers.reshape((k, d));
	clusters = [[] for _ in range(k)];
	distances = [];
	for i in range(n):
		min_distance = minkowski(data[i], centers[0], 2);
		idx = 0;
		for j in range(1, k):
			d_temp = minkowski(data[i], centers[j], 2);
			if(d_temp < min_distance):
				min_distance = d_temp;
				idx = j;
		clusters[idx].append(i);
		distances.append(min_distance);
	return clusters, distances;

def GetNewCenter(p):
	c = np.mean(p, axis=0);
	for _ in range(20):
		num, den = 0, 0;
		for pi in p:
			norm = minkowski(pi, c, 2);
			num += pi / norm;
			den += 1 / norm;
		c = num / den;
	return c;

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

# Optimize function
clusters_prev, distances = GetClusters(centers);
print("Current function value: %.3f" %np.sum(distances));

stop_criteria = False;
iteration = 1;
while(stop_criteria == False):
	for i in range(k):
		current_cluster = data[clusters_prev[i]];
		centers[i] = GetNewCenter(current_cluster);
	clusters_new, distances = GetClusters(centers);
	print("Iteration %d, current function value: %.3f"
		%(iteration, np.sum(distances)));
	if(clusters_prev == clusters_new):
		stop_criteria = True;
		print("Local optimum reached");
	clusters_prev = clusters_new;
	iteration += 1;

# Show results
clusters, distances = GetClusters(centers);
labels = np.zeros(n, dtype=int);
for i in range(len(clusters)):
	for p in clusters[i]:
		labels[p] = i;

print("Adjusted mutual information: %.3f %%"
	%(100 * metrics.adjusted_mutual_info_score(target, labels)));

print("\nTotal time = "+str(tm.time()-start_time)+" s");

print("\nK-means:");
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=k, random_state=0).fit(data);
print("Adjusted mutual information: %.3f %%"
	%(100 * metrics.adjusted_mutual_info_score(target, kmeans.labels_)));