import numpy as np;
import time as tm;
from scipy.spatial import distance;
from scipy.optimize import minimize;
from sklearn import metrics;

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

def InterClusterDistance(c):
	dist = 0;
	for pi in current_cluster:
		dist += np.sqrt(np.sum([d*d for d in pi-c]));
	return dist;

def GetCenter(p, c):
	res = minimize(InterClusterDistance, c, method='BFGS', options={'disp': True});
	return res.x;

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
#centers = centers.flatten();

# Optimize function
clusters_prev, distances = GetClusters(centers);
print("Current function value: %.3f" %np.sum(distances));

stop_criteria = False;
iteration = 1;
while(stop_criteria == False):
	for i in range(k):
		current_cluster = data[clusters_prev[i]];
		centers[i] = GetCenter(current_cluster, centers[i]);
	clusters_new, distances = GetClusters(centers);
	print("Iteration %d, current function value: %.3f"
		%(iteration, np.sum(distances)));
	if(clusters_prev == clusters_new):
		stop_criteria = True;
		print("Local optimum reached");
	clusters_prev = clusters_new;
	iteration += 1;

# Show results

#print("Centers found:");
#print(centers.reshape((k, d)));
clusters, distances = GetClusters(centers);
labels = np.zeros(n, dtype=int);
for i in range(len(clusters)):
	for p in clusters[i]:
		labels[p] = i;

print("Adjusted mutual information: %.3f %%" %(100 * metrics.adjusted_mutual_info_score(target, labels)));

print("\nTotal time = "+str(tm.time()-start_time)+" s");

print("\nK-means:");
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=k, random_state=0).fit(data);
print("Adjusted mutual information: %.3f %%" %(100 * metrics.adjusted_mutual_info_score(target, kmeans.labels_)));