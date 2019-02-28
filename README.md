# Clustering
Three algorithms are tested:
* K-means
* Emax
* SSO Clustering (proposed)

## Compiling and running

### K-Means

The K-Means algorithm is written in C in just one file: `k-means.c`. To compile it, run

`gcc -o <exe> k-means.c`

To execute it:

`<exe> < <dataset_path> <scaling_argument>`

Where:
* `<dataset_path>`: Path to the dataset file formatted as specified.
* `<exe>`: Name of the executable file.
* `<scaling_argument>`: Some non empty argument for Z-score normalization, empty argument for no scaling.

### Emax

The Emax algorithm is written in C in just one file: `emax.c`. To compile it, run

`gcc -o <exe> emax.c`

To execute it:

`<exe> < <dataset_path> <scaling_argument>`

Where:
* `<dataset_path>`: Path to the dataset file formatted as specified.
* `<exe>`: Name of the executable file.
* `<scaling_argument>`: Some non empty argument for Z-score normalization, empty argument for no scaling.

### SSO-Clustering

The SSO-Clustering algorithm is written in C in just one file: `SSO-clustering.c`. To compile it, run

`gcc -o <exe> SSO-clustering.c`

To execute it:

`<exe> < <dataset_path> <number_spiders> <approx_population> <iterations> <alpha>`

Where:
* `<dataset_path>`: Path to the dataset file formatted as specified.
* `<number_spiders>`: Number of biological agents to emulate (10, 50, 100, etc.). Defalult: 100.
* `<approx_population>`: Percentage of biological agents initialized with an approximation algorithm (5, 8, 10, etc.) in [0, 100]. Default: 10.
* `<iterations>`: Number of iterations (1, 10, 50, 100, 500, etc.). Default: 100.
* `<alpha>`: Normalization parameter in [0, 1]. Default: 0.5.