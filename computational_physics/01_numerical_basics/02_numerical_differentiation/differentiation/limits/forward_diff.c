#include<stdio.h>
#include<math.h>
int main(void)
{
	double x;
	printf("Enter a value (x) in radians: ");
	scanf("%lf", &x);

	double h;
	printf("Enter size : ");
	scanf("%lf", &h);

	double y = (sin(x + h) - sin(x)) / h;
	double z = cos(x);
	double error = z - y;

	printf("Analytical value: cos(x) = %.17f\n", y);
	printf("Exact value: cos(x) = %.17f\n", z);
	printf("Error in the values = %.17f\n", error);

	return 0;
}
