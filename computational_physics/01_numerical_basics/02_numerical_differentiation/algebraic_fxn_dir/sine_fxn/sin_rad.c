#include<stdio.h>
#include<math.h>

int main(void)

{
	double x;

	printf("Following function is in radians!!\n");
	printf("Enter x: ");
	scanf("%lf", &x);

	printf("sin(x) = %.17f \n", sin(x));

	return 0;
}


