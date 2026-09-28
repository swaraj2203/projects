#include<stdio.h>
#include<math.h>
int main(void)
{

	double x;
	printf("Enter a value for x (in radians): ");
	scanf("%lf", &x);

	double h;
	printf("Enter step size h: ");
	scanf("%lf", &h);

	double exact = cos(x);

	double analytical = (sin(x) - sin(x - h)) / h;

	double error = exact - analytical;

	printf("Exact value is cos(x) = %.17f\n", exact);
	printf("Analytical value is cos(x) = %.17f\n", analytical);
	printf("Difference in the two values is = %.17f\n", error);

	return 0;
}
