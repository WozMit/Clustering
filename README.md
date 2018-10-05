# Clustering
Three algorithms are tested:
* K-means
* EM
* SSO Clustering

## Compiling and running

### K-Means

The K-Means algorithm is written in C in just one file: `k-means.c`. To compile it, run

`gcc -o <executable_name> k-means.c`

To execute it:

`<executable_name> < <dataset_path> <scaling_argument>`

Where:
* `<dataset_path>`: Path to the dataset file formatted as specified
* `<scaling_argument>`: Some non empty argument for Z-score normalization, empty argument for no scaling