# Clustering
Three algorithms are tested:
* K-means
* EM
* SSO Clustering

## Compiling

### K-Means

The K-Means algorithm is written in C in just one file: `k-means.c`. To compile it, run

`gcc -o <executable_name> k-means.c`

For executing:

`<executable_name> < <dataset_path> <scaling_argument>`

Where:
* `<dataset_path>`: Path to the dataset file formatted as specified
* `<scaling_argument>`: Some non empty argument for Z-scaling, empty for no scaling