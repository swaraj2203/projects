#include<stdio.h>
#include<math.h>
int main(void)
{
	double x;
	printf("Enter a value for x (in radians): ");
	scanf("%lf", &x);

	double exact = cos(x);

	int forward_done  = 0;
	int backward_done = 0;
	int central_done  = 0;

	FILE *file = fopen("data.txt", "w");

	for (int i = 0; i <= 16; i++)
	{
		double h = pow(10, -i);

		double forward = (sin(x + h) - sin(x)) / h;
		double forward_error = exact - forward;
		if (!forward_done && fabs(forward_error) < 1e-10)
			{
			 	forward_done = 1;
				printf("Forward difference reached tolerance at h = %.1e\n", h);
			}

		double backward = (sin(x) - sin(x - h)) / h;
		double backward_error = exact - backward;
		if (!backward_done && fabs(backward_error) < 1e-10)
			{
				backward_done = 1;
				printf("Backward difference reached tolerance at h = %.1e\n", h);
			}

		double central = (sin(x + h) - sin(x - h)) / (2*h);
		double central_error = exact - central;
		if (!central_done && fabs(central_error) < 1e-10)
			{
				central_done = 1;
				printf("Central difference reached tolerance at h = %.1e\n", h);
			}

		if (forward_done && backward_done && central_done)
			{
				break;
			}

		fprintf(file, "%d %.17f %.17f %.17f %.17f\n", i, h, forward_error, backward_error, central_error);
	}

	fclose(file);

	return 0;
}
