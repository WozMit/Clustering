import numpy as np;
from sklearn import metrics;

# Read the last line of the output file
with open('output') as openfileobject:
	t = [line[:-2] for line in openfileobject];
a = np.array([int(x) for x in t[-2].split(' ')]);
b = np.array([int(x) for x in t[-1].split(' ')]);

# Get AMI score
ami = metrics.adjusted_mutual_info_score(a, b);
print("Adjusted mutual information: %.5f" %ami);