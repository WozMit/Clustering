#include <stdio.h>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <stdbool.h>
int dk;

double random(){
	return (double)rand() / (double)RAND_MAX;
}

double J(double *x){
	double sum = 0;
	int i;
	for(i=0; i<dk-1; i++)
		sum += 100.0 * pow(x[i + 1] - x[i]*x[i], 2) + pow(1.0 - x[i], 2);
	return sum;
}

int main(int argc, char const *argv[]){
	clock_t _start = clock();
	dk = 12;
	int low[dk], high[dk];
	int i, j, dim;
	for(i=0; i<dk; i++){
		low[i] = -10;
		high[i] = 10;
	}

	// Initialize the parameters
	srand(0);
	int numbSpiders = 100;
	int numbF = (0.9 - random() * 0.25) * numbSpiders;
	int numbM = numbSpiders - numbF;
	double PF = 0.7;

	// Initialize the spider values
	double r = 0, spiders[numbSpiders][dk];
	for(j=0; j<dk; j++) r += high[j] - low[j];
	r /= 2.0 * numbSpiders;
	for(i=0; i<numbSpiders; i++)
		for(j=0; j<dk; j++){
			spiders[i][j] = low[j] + random() * (high[j] - low[j]);
		}

	// Execute the algorithm
	bool stopCriteria = false;
	while(stopCriteria == false){
		// Calculate the weight of every spider
		double weight[numbSpiders], bestVal, worstVal;
		int sc, sb;
		for(i=0; i<numbSpiders; i++){
			weight[i] = J(spiders[i]);
			if(i == 0) bestVal = worstVal = weight[0];
			if(weight[i] < bestVal) bestVal = weight[i], sb = i;
			if(weight[i] > worstVal) worstVal = weight[i];
		}
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
					distance = sqrt(distance);
					if(miniDistance == -1.0 || distance < miniDistance){
						miniDistance = distance;
						vibci = weight[j] * exp(-miniDistance);
						sc = j;
					}
				}
			if(i == sb) sc = i;
			double vibbi = 0.0;
			for(dim=0; dim<dk; dim++)
				vibbi += pow(spiders[i][dim] - spiders[sb][dim], 2);
			vibbi = exp(-sqrt(vibbi));
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
		for(i=numbF; i<numbSpiders; i++){
		}
		stopCriteria = true;
	}
	printf("%30c Executed in %.3f s.",
		32, (double)(clock() - _start)/CLOCKS_PER_SEC);
	return 0;
}