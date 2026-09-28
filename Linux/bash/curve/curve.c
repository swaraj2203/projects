#include <stdio.h>
#include <math.h>

int main(void)
{
	const double xmax = 30.0;
	const double dx = 0.001;

	FILE *file = fopen("curve.dat", "w");

	if (file == NULL)
	{
		printf("Could not open curve.dat\n");
		return 1;
	}

	for (double x = 0.0; x <= xmax; x += dx)
	{
		double y = exp(-0.06 * x) * (sin(x * x) + 0.35 * sin(3.7 * x));

		fprintf(file, "%f %f\n", x, y);
	}

	fclose(file);

	printf("Data generation complete. \n");

	return 0;

}
