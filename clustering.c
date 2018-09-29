#include <stdio.h>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <stdbool.h>
int n, d, k;

double random(){
	return (double)rand() / (double)RAND_MAX;
}

double J(double *distances){
	double cost = 0.0;
	int i;
	for(i=0; i<n; i++) cost += distances[i];
	return cost;
}

int main(int argc, char const *argv[]){
	clock_t _start = clock();
	// Read the initial data
	scanf("%d %d %d", &n, &d, &k);
	double data[n][d];
	int i, j, dim, labels[n];
	for(i=0; i<n; i++){
		for(j=0; j<d; j++){
			double x; scanf("%lf", &x);
			data[i][j] = x;
		}
		int x; scanf("%d", &x);
		labels[i] = x;
	}

	// Print the data
	/*printf("%d %d %d\n", n, d, k);
	for(i=0; i<n; i++){
		for(j=0; j<d; j++) printf("%lf ", data[i][j]);
		printf("%d\n", labels[i]);
	}*/

	// Generate initial centers
	srand(0);
	double centers[k][d], lowers[d], uppers[d];
	for(j=0; j<d; j++) lowers[j] = uppers[j] = data[0][j];
	for(i=1; i<n; i++)
		for(j=0; j<d; j++){
			if(data[i][j] < lowers[j]) lowers[j] = data[i][j];
			if(data[i][j] > uppers[j]) uppers[j] = data[i][j];
		}
	for(i=0; i<k; i++)
		for(j=0; j<d; j++)
			centers[i][j] = lowers[j] + random() * (uppers[j] - lowers[j]);

	// Denle this
	/*centers[0][0] = 5.01213868;
	centers[0][1] = 3.40310154;
	centers[0][2] = 1.47163904;
	centers[0][3] = 0.23540679;

	centers[1][0] = 5.93432784;
	centers[1][1] = 2.79779913;
	centers[1][2] = 4.41789295;
	centers[1][3] = 1.4172667;

	centers[2][0] = 6.73334675;
	centers[2][1] = 3.0678501;
	centers[2][2] = 5.6300751;
	centers[2][3] = 2.10679832;*/

	// Generate clusters
	int labels_pred[n];
	double distances[n];
	for(j=0; j<n; j++) distances[j] = 1<<30;
	for(i=0; i<n; i++){
		for(j=0; j<k; j++){
			// Calculate distance from point Pi to center cj
			double distance = 0.0;
			for(dim=0; dim<d; dim++)
				distance += pow(data[i][dim] - centers[j][dim], 2);
			distance = sqrt(distance);
			if(distance < distances[i]){
				distances[i] = distance;
				labels_pred[i] = j;
			}
		}
	}
	for(i=0; i<n; i++) printf("%d ", labels_pred[i]);
	printf("\n");
	printf("%lf\n", J(distances));
	printf("%30c Executed in %.3f s.",
		32, (double)(clock() - _start)/CLOCKS_PER_SEC);
	return 0;
}
