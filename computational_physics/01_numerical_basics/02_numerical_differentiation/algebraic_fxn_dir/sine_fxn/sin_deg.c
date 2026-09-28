#include<stdio.h>
#include<math.h>

int main(void)
{
	double x;

	printf("This function is in degrees!!\n");
	printf("Enter x: ");
	scanf("%lf", &x);

	double result =sin(x * (M_PI/180));

	printf("sin(x) = %.17f \n", result);

	return 0;
}
