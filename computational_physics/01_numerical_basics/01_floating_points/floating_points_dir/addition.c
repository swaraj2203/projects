#include<stdio.h>

int main(void)
{

	double x = 0.0;

	for (int i = 0; i < 10; i++)
	{
		x += 0.1;
		printf("%.17f \n", x);
	}

	return 0;
}
