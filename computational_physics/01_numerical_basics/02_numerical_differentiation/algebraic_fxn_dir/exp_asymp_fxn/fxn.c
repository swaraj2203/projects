#include<stdio.h>
#include<math.h>
int main(void)
{
	double xmin = -2;
	double xmax =  2;

	double ymin = 0.1;
	double ymax = 10;

	double zmin = -2;
	double zmax =  2;

	int N = 10000;

	double dx = (xmax - xmin) / (N - 1);

	double dy = (ymax - ymin) / (N - 1);

	double dz = (zmax - zmin) / (N - 1);

	FILE *file = fopen("exp_asympt_data.txt","w");

	for(int i = 0; i < N; i++)
	{
		double x = xmin + i * dx;
		double x_out = exp(x);

		double y = ymin + i * dy;
		double y_out = log(y);

		double z = zmin + i * dz;
		double z_out = 1 / z;

		fprintf(file, "%.17f %.17f %.17f %.17f %.17f %.17f \n", x, x_out, y, y_out, z, z_out);
	}

	fclose(file);

	return 0;
}
