import numpy as np;
from sklearn import metrics;

import matplotlib.pyplot as plt;
from mpl_toolkits.mplot3d import Axes3D;
from sklearn.decomposition import PCA;

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

# Read the last line of the output file
with open('output') as openfileobject:
	t = [line[:-2] for line in openfileobject];
a = np.array([int(x) for x in t[-2].split(' ')]);
b = np.array([int(x) for x in t[-1].split(' ')]);

# Get AMI score
ami = metrics.adjusted_mutual_info_score(a, b);
print("Adjusted mutual information: %.5f" %ami);

#ShowIris(data, a, "Global optimization algorithm");