#include <stdio.h>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <stdbool.h>
int n, d, k;

double random(){
	return (double)rand() / (double)RAND_MAX;
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

	// Generate initial clusters
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

	// Iterate the algorithm
	bool stopCriteria = false;
	double bestSoFar;
	int iteration = 0, temp_labels[n];
	while(stopCriteria == false){
		printf("Iteration %d\n", ++iteration);

		// Calculate new centers
		int sizes[k];
		for(i=0; i<k; i++){
			for(j=0; j<d; j++) centers[i][j] = 0;
			sizes[i] = 0;
		}
		for(i=0; i<n; i++){
			for(j=0; j<d; j++)
				centers[ labels_pred[i] ][j] += data[i][j];
			sizes[ labels_pred[i] ]++;
		}
		for(i=0; i<k; i++)
			for(j=0; j<d; j++) centers[i][j] /= sizes[i];

		// Generate new clusters
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
					temp_labels[i] = j;
				}
			}
		}

		// Check if clusters did not change
		stopCriteria = true;
		for(i=0; i<n && stopCriteria; i++)
			if(temp_labels[i] != labels_pred[i]) stopCriteria = false;
		for(i=0; i<n; i++) labels_pred[i] = temp_labels[i];

		// Calculate the current function value and save if possible
		double cost = 0.0;
		for(i=0; i<n; i++) cost += pow(distances[i], 2);
		if(iteration == 1 || cost < bestSoFar)
			bestSoFar = cost;

		// Show state information
		printf("Current function value: %.5f\n", cost);
		printf("\n");
	}
	printf("Centers found:\n");
	for(i=0; i<k; i++){
		for(j=0; j<d; j++) printf("%lf ", centers[i][j]);
		printf("\n");
	}
	printf("\nBest function value: %.5f\n", bestSoFar);
	printf("%30c Executed in %.3f s.",
		32, (double)(clock() - _start)/CLOCKS_PER_SEC);
	printf("\n\n");
	for(i=0; i<n; i++) printf("%d ", labels_pred[i]);
	printf("\n");
	for(i=0; i<n; i++) printf("%d ", labels[i]);
	printf("\n");
	return 0;
}
