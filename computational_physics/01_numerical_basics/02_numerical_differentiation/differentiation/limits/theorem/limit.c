#include<stdio.h>
#include<math.h>
int main(void)
{
	double x;
	printf("Enter a value for x (in radians): ");
	scanf("%lf", &x);

	double exact = cos(x);
	printf("Exact derivative: cos(x) = %.17f \n", exact);

	FILE *file = fopen("data.txt","w");

	for(int i = 1; i <= 13; i++)
	{
		double h = pow(10, -i);

		double analytical = (sin(x + h) - sin(x)) / h;

		double error = exact - analytical;

		fprintf(file,"%d %.17f %.17f %.17f \n", i, exact, analytical, error);

	}

	fclose(file);

	return 0;
}
