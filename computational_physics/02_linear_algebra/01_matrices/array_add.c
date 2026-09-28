#include<stdio.h>
#include<math.h>
int main(void)
{

	double v[3] = {2.0, -1.0, 4.0};
	double w[3] = {2.9, -3.2, 0.9};

	double add[3];

	for (int i = 0; i < 3; i++)
	{
		add[i] = v[i] + w[i];
	}

	printf("Addition of two arrays: \n");

	for (int i = 0; i < 3 ; i++)
	{
		printf("%f\n", add[i]);
	}

	return 0;
}
