#include <stdio.h>
#include <math.h>

int main(void)
{
	/*Physical constants*/
	const double G = 6.67340e-11;
	const double M_sun = 1.98847e30;
	const double AU = 1.495978707e11;

	/*Range of distances*/
	const double r_min = 0.1;
	const double r_max = 40.0;

	/*Number of points*/
	const int N = 1000;

	/*Output file */
	FILE *file = fopen("orbit.dat", "w");

	if (file == NULL)
	{
		printf("Error : could not open orbit.dat\n");
		return 1;
	}

	/*Calculation*/

	for (int i = 0; i < N; i++)
	{
		double r_AU = r_min + (r_max - r_min) * i / (N-1);
		double r_m = r_AU * AU;
		double v_ms = sqrt(G * M_sun / r_m);
		double v_kms = v_ms / 1000.0;
		fprintf(file, "%f %f\n", r_AU, v_kms);
	}

	fclose(file);
	printf("Calculations complete. \n");
	printf("Results written to orbit.dat\n");

	return 0;
}
