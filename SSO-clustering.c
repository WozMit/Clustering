#include <stdio.h>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <stdbool.h>
int n, d, k;
double **data, **centers, coef1, coef2;

double random(){
	return (double)rand() / (double)RAND_MAX;
}

int cmpfunc(const void *a, const void *b){
	if (*(double*)a > *(double*)b) return 1;
	else if (*(double*)a < *(double*)b) return -1;
	return 0;
}

double J(double *x){
	// Form centers
	int i, j, dim, idx = 0;
	for(i=0; i<k; i++)
		for(j=0; j<d; j++) centers[i][j] = x[idx++];
	// Generate clusters
	double distances[n];
	for(j=0; j<n; j++) distances[j] = 1<<30;
	for(i=0; i<n; i++){
		for(j=0; j<k; j++){
			// Calculate distance from point Pi to center cj
			double distance = 0.0;
			for(dim=0; dim<d; dim++)
				distance += pow(data[i][dim] - centers[j][dim], 2);
			distance = sqrt(distance);
			if(distance < distances[i])
				distances[i] = distance;
		}
	}
	double sum1 = 0.0, sum2 = 0.0;
	for(i=0; i<n; i++){
		sum1 += distances[i] * distances[i];
		sum2 += distances[i];
	}
	return coef1 * sum1 + coef2 * sum2;
}

int main(int argc, char const *argv[]){
	clock_t _start = clock();
	// Read the data
	scanf("%d %d %d", &n, &d, &k);
	int i, j, dim, labels[n];
	data = (double **)malloc(n * sizeof(double*));
	for(i=0; i<n; i++) data[i] = (double *)malloc(d * sizeof(double));
	centers = (double **)malloc(k * sizeof(double*));
	for(i=0; i<k; i++) centers[i] = (double *)malloc(d * sizeof(double));
	for(i=0; i<n; i++){
		for(j=0; j<d; j++){
			double x; scanf("%lf", &x);
			data[i][j] = x;
		}
		int x; scanf("%d", &x);
		labels[i] = x;
	}

	// Generate initial centers
	srand(time(NULL));
	double lowers[d], uppers[d];
	for(j=0; j<d; j++) lowers[j] = uppers[j] = data[0][j];
	for(i=1; i<n; i++)
		for(j=0; j<d; j++){
			if(data[i][j] < lowers[j]) lowers[j] = data[i][j];
			if(data[i][j] > uppers[j]) uppers[j] = data[i][j];
		}
	for(i=0; i<k; i++)
		for(j=0; j<d; j++)
			centers[i][j] = lowers[j] + random() * (uppers[j] - lowers[j]);

	int dk = d * k, idx, idx1;
	double low[dk], high[dk];
	for(i=0; i<dk; i+=d)
		for(j=0; j<d; j++){
			low[i + j] = lowers[j];
			high[i + j] = uppers[j];
		}

	// Read arguments
	int numbSpiders = 100, greedy = 10, max_iterations = 100;
	coef1 = 0.5;
	if(argc == 5){
		sscanf(argv[1], "%d", &numbSpiders);
		sscanf(argv[2], "%d", &greedy);
		sscanf(argv[3], "%d", &max_iterations);
		sscanf(argv[4], "%lf", &coef1);
	}
	coef2 = 1.0 - coef1;

	// Initialize the parameters
	int numbF = (0.9 - random() * 0.25) * numbSpiders;
	int numbM = numbSpiders - numbF;
	double PF = 0.7;

	// Initialize the spider values
	double r = 0, spiders[numbSpiders][dk], distances[n];
	// Greedy k-center
	greedy = greedy * numbSpiders / 100;
	for(idx1=0; idx1<greedy; idx1++){
		int pos = 0, head = random() * n;
		for(i=0; i<d; i++) spiders[idx1][pos++] = data[head][i];
		for(i=0; i<n; i++){
			double distance = 0.0;
			for(dim=0; dim<d; dim++)
				distance += pow(data[i][dim] - data[head][dim], 2);
			distance = sqrt(distance);
			distances[i] = distance;
		}
		for(idx=1; idx<k; idx++){
			double maxiDistance = 0.0;
			for(i=0; i<n; i++)
				if(distances[i] > maxiDistance){
					maxiDistance = distances[i];
					head = i;
				}
			for(i=0; i<d; i++) spiders[idx1][pos++] = data[head][i];
			for(i=0; i<n; i++){
				double distance = 0.0;
				for(dim=0; dim<d; dim++)
					distance += pow(data[i][dim] - data[head][dim], 2);
				distance = sqrt(distance);
				if(distance < distances[i]) distances[i] = distance;
			}
		}
	}

	// Random initialization
	for(j=0; j<dk; j++) r += high[j] - low[j];
	r /= 2 * dk;
	for(i=greedy; i<numbSpiders; i++)
		for(j=0; j<dk; j++){
			spiders[i][j] = low[j] + random() * (high[j] - low[j]);
		}

	// Execute the algorithm
	bool stopCriteria = false;
	double bestSpider[dk], bestSoFar;
	int iteration = 0;
	while(stopCriteria == false){
		printf("Iteration %d\n", ++iteration);
		// Calculate the weight of every spider
		double weight[numbSpiders], bestVal, worstVal, maxDistance = -1.0;
		int sc, sb = 0, sf;
		for(i=0; i<numbSpiders; i++){
			weight[i] = J(spiders[i]);
			if(i == 0) bestVal = worstVal = weight[0];
			if(weight[i] < bestVal) bestVal = weight[i], sb = i;
			if(weight[i] > worstVal) worstVal = weight[i];
			for(j=i+1; j<numbSpiders; j++){
				double distance = 0.0;
				for(dim=0; dim<dk; dim++)
					distance += pow(spiders[i][dim] - spiders[j][dim], 2);
				if(maxDistance == -1.0 || distance > maxDistance)
					maxDistance = distance;
			}
		}
		maxDistance = sqrt(maxDistance) / 1.5;
		for(i=0; i<numbSpiders; i++)
			weight[i] = (weight[i] - worstVal) / (bestVal - worstVal);

		// Move female spiders according to the female cooperative operator
		for(i=0; i<numbF; i++){
			// Calculate vibci and vibbi
			double vibci, miniDistance = -1.0;
			for(j=0; j<numbSpiders; j++)
				if(weight[j] > weight[i]){
					double distance = 0.0;
					for(dim=0; dim<dk; dim++)
						distance += pow(spiders[i][dim] - spiders[j][dim], 2);
					distance = sqrt(distance) / maxDistance;
					if(miniDistance == -1.0 || distance < miniDistance){
						miniDistance = distance;
						vibci = weight[j] / exp(miniDistance*miniDistance);
						sc = j;
					}
				}
			if(i == sb) sc = i;
			double vibbi = 0.0;
			for(dim=0; dim<dk; dim++)
				vibbi += pow(spiders[i][dim] - spiders[sb][dim], 2);
			vibbi = sqrt(vibbi) / maxDistance;
			vibbi = weight[sc] / exp(vibbi*vibbi);
			// Perform movement
			double alpha = random(), beta = random(), delta = random();
			if(random() < PF) alpha = -alpha, beta = -beta;
			for(dim=0; dim<dk; dim++)
				spiders[i][dim] +=
					alpha * vibci * (spiders[sc][dim] - spiders[i][dim])
					+ beta * vibbi * (spiders[sb][dim] - spiders[i][dim])
					+ delta * (random() - 0.5);
		}

		// Move male spiders according to the male cooperative operator
		// Get the median male weight
		double temp[(numbM > dk ? numbM:dk)];
		for(i=numbF; i<numbSpiders; i++) temp[i-numbF] = weight[i];
		qsort(temp, numbM, sizeof(double), cmpfunc);
		double wmedianMale = temp[numbM / 2];
		// Get the weighted mean of the male population
		double sumwMale = 0.0;
		for(j=0; j<dk; j++) temp[j] = 0;
		for(i=numbF; i<numbSpiders; i++){
			for(j=0; j<dk; j++)
				temp[j] += spiders[i][j] * weight[i];
			sumwMale += weight[i];
		}
		for(j=0; j<dk; j++) temp[j] /= sumwMale;
		// Iterate over all males
		for(i=numbF; i<numbSpiders; i++){
			double alpha = random(), delta = random();
			if(weight[i] > wmedianMale){
				// Calculate vibfi
				double vibfi, miniDistance;
				for(j=0; j<numbF; j++){
					double distance = 0.0;
					for(dim=0; dim<dk; dim++)
						distance += pow(spiders[i][dim] - spiders[j][dim], 2);
					distance = sqrt(distance) / maxDistance;
					if(j == 0 || distance < miniDistance){
						miniDistance = distance;
						vibfi = weight[j] / exp(miniDistance*miniDistance);
						sf = j;
					}
				}
				// Perform movement
				for(dim=0; dim<dk; dim++)
					spiders[i][dim] +=
						alpha * vibfi * (spiders[sf][dim] - spiders[i][dim])
						+ delta * (random() - 0.5);
			}
			else
				for(dim=0; dim<dk; dim++)
					spiders[i][dim] += alpha * (temp[dim] - spiders[i][dim]);
		}

		// Perform mating operation
		for(i=numbF; i<numbSpiders; i++)
			if(weight[i] > wmedianMale){
				int T[numbF], idx = 1;
				T[0] = i;
				sumwMale = weight[i];
				for(j=0; j<numbF; j++){
					double distance = 0.0;
					for(dim=0; dim<dk; dim++)
						distance += pow(spiders[i][dim] - spiders[j][dim], 2);
					if(sqrt(distance) <= r){
						T[idx++] = j;
						sumwMale += weight[j];
					}
				}
				if(idx > 1){
					// Form the brood in temp
					for(dim=0; dim<dk; dim++) temp[dim] = 0.0;
					for(j=0; j<idx; j++)
						for(dim=0; dim<dk; dim++)
							temp[dim] += spiders[ T[j] ][dim] *
									weight[ T[j] ] / sumwMale;
					sumwMale = (J(temp) - worstVal) / (bestVal - worstVal);
					// Find the worst spider
					double worstWeight = -1.0;
					idx = 0;
					for(j=0; j<numbSpiders; j++)
						if(j == 0 || weight[j] < worstWeight){
							worstWeight = weight[j];
							idx = j;
						}
					if(sumwMale > weight[idx]){
						// Replace worst spider
						for(dim=0; dim<dk; dim++)
							spiders[idx][dim] = temp[dim];
						weight[idx] = sumwMale;
					}
				}
			}

		// Save or show some results
		if(iteration == max_iterations) stopCriteria = true;
		bestVal = J(spiders[0]);
		int spider = 0;
		for(i=1; i<numbSpiders; i++){
			sumwMale = J(spiders[i]);
			if(sumwMale < bestVal){
				bestVal = sumwMale;
				spider = i;
			}
		}
		if(iteration == 1 || bestVal < bestSoFar){
			bestSoFar = bestVal;
			for(j=0; j<dk; j++) bestSpider[j] = spiders[spider][j];
		}
		printf("Current function value: %.5f\n", bestVal);
		printf("\n");
	}
	printf("Best function value: %.5f\n", bestSoFar);
	printf("Best spider:\n");
	// Form centers
	idx = 0;
	for(i=0; i<k; i++)
		for(j=0; j<d; j++) centers[i][j] = bestSpider[idx++];
	for(i=0; i<k; i++){
		for(j=0; j<d; j++) printf("%lf ", centers[i][j]);
		printf("\n");
	}

	// Generate clusters
	int labels_pred[n];
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
	for(i=0; i<n; i++) free(data[i]);
	free(data);
	for(i=0; i<k; i++) free(centers[i]);
	free(centers);
	printf("%30c Executed in %.0f ms.\n",
		32, 1000.0*(double)(clock() - _start)/CLOCKS_PER_SEC);
	for(i=0; i<n; i++) printf("%d ", labels[i]);
	printf("\n");
	for(i=0; i<n; i++) printf("%d ", labels_pred[i]);
	printf("\n");
	return 0;
}
