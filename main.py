import os;
import numpy as np;
from sklearn import metrics;
import matplotlib.pyplot as plt;
from mpl_toolkits.mplot3d import Axes3D;
from sklearn.decomposition import PCA;

def PlotDataset(x, y, title=""):
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

# Get a dataset list
datasets = [];
for dir_name, sub_dir_list, dir_file_list in os.walk('datasets'):
	for file in dir_file_list:
		if(len(file) > 3 and file[-4:] == '.woz'):
			datasets.append(os.path.join(dir_name, file));

# Compile command
#os.system('gcc -o a k-means.c');
#os.system('gcc -o a emax.c');
os.system('gcc -o a SSO-clustering.c');

# Execute command
dataset = "datasets\\iris.woz";
command = "a < " + dataset + " 100 10 100 0.2 > output";
#command = "a < " + dataset + " > output";

for _ in range(50):
	os.system(command);

	# Read the last line of the output file
	with open('output') as file:
		lines = [line[:-2] for line in file];
		file.close();
	a = np.array([int(x) for x in lines[-2].split(' ')]);
	b = np.array([int(x) for x in lines[-1].split(' ')]);

	# Get AMI score
	ami = metrics.adjusted_mutual_info_score(a, b);
	print("Adjusted mutual information: %.5f" %ami);

# Read the dataset
"""with open(cancer_dataset) as file:
	lines = [line[:-1] for line in file];
	file.close();
n, d, k = map(int, lines[0].split(' '));
data = np.zeros((n, d));
labels_true = np.zeros(n);
for i in range(n):
	x = [float(x) for x in lines[i+1].split(' ')];
	data[i] = x[:d];
	labels_true[i] = x[d];
labels_true = labels_true.astype(int);

# Scale the data
data = (data - np.mean(data))/np.std(data);

# Plot the dataset in 3d
PlotDataset(data, labels_true);"""