#include <stdio.h>
#include <math.h>

double f1(double u, double du)
{
	return du;
}

double f2(double u, double p, double epsilon)
{
	return 1.0 / p + epsilon * u * u - u;
}

int main(void)
{
	const double p = 1.0;
	const double e = 0.3;
	const double epsilon = 0.01;

	const double phi_max = 200.0 * M_PI;
	const double h = 0.001;

	double u = (1.0 + e) / p;
	double du = 0.0;

	FILE *file = fopen("orbit.dat","w");

	if (file == NULL)
	{
		printf("Could not open orbit.dat\n");
		return 1;
	}

	for (double phi = 0.0; phi <= phi_max; phi += h)
	{

		if (u <= 0.0)
		{
			printf("Simulation became unstable at phi = %f\n", phi);
			break;
		}

		double r = 1.0 / u;

		double x = r * cos(phi);
		double y = r * sin(phi);

		fprintf(file, "%f %f\n", x, y);

		/*Runge-Kutta method*/

		double k1_u = h * f1(u, du);
		double k1_du = h * f2(u, p, epsilon);

		double k2_u = h * f1(
			u + 0.5 * k1_u,
			du + 0.5 * k1_du
		);

		double k2_du = h * f2(
			u + 0.5 * k1_u,
			p,
			epsilon
		);

		double k3_u = h * f1(
			u + 0.5 * k2_u,
			du + 0.5 * k2_du
		);

		double k3_du = h * f2(
			u + 0.5 * k2_u,
			p,
			epsilon
		);

		double k4_u = h * f1(
			u + k3_u,
			du + k3_du
		);

		double k4_du = h * f2(
			u + k3_u,
			p,
			epsilon
		);

		u += (k1_u + 2.0 * k2_u + 2.0 * k3_u + k4_u) / 6.0;

		du += (k1_du + 2.0 * k2_du + 2.0 * k3_du + k4_du) / 6.0;

	}

	fclose(file);

	return 0;

}
