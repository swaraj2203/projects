#include<stdio.h>
#include<math.h>

int main (void)
{
	double xmin = -5*M_PI;
	double xmax = 5*M_PI;
	int N = 1000;

	double dx = (xmax - xmin) / N;

	FILE *file = fopen("Sine_curve.txt","w");

	for(int i = 0; i < N; i++)
	{
		double x = xmin + i * dx;
		double y = sin(x);
		fprintf(file,"%.17f %.17f\n", x, y);
	}

	fclose(file);

	return 0;
}
