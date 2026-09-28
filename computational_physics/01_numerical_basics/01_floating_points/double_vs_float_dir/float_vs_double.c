#include<stdio.h>

int main(void)
{

	double x = 0.0;
	float  y = 0.0;

	FILE *file = fopen("error_acc_data.txt", "w");

	if (file == NULL)
	{
		printf("Could not open file \n");
		return 1;
	}

	fprintf(file, "i double float double_error float_error\n");

	for (int i=0; i<101; i++)
	{
		x += 0.1;
		y += 0.1;

		double double_error = x - ((1+i)/10.0);
		double float_error  = y - ((1+i)/10.0);

		fprintf(file, "%d %.17f %.17f %.17f %.17f \n",
				i+1, x, y, double_error, float_error);
	}

	fclose(file);

	return 0;

}
