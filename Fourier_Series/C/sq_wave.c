#include<stdio.h>
#include<math.h>

int main() {
	double pi = 3.141592653589793;

	double N = 1000;
	double terms = 50;

	double x[1000];
	double y[1000];

	for (int i = 0; i < N; i++){
		x[i] = -3*pi + i*(6*pi/N);

		double sum = 0.0;

		for (int n = 1; n < terms; n += 2){ //odd terms only
			sum += (4.0/(n*pi)) * sin(n*x[i]);
		}

		y[i] = sum;
	}
	FILE *f = fopen("Square.dat","w");

	for (int i = 0; i < N; i++){
		fprintf(f, "%f %f\n", x[i], y[i]);
	}

	fclose(f);

	// Automatically generate plot using gnuplot

	FILE *gnuplotPipe = popen("gnuplot -persistent", "w");

	fprintf(gnuplotPipe, "set title 'Square Wave Fourier Series'\n");
	fprintf(gnuplotPipe, "set xlabel 'x'\n");
	fprintf(gnuplotPipe, "set ylabel 'f(x)'\n");
	fprintf(gnuplotPipe, "set zeroaxis\n");
	fprintf(gnuplotPipe, "set xrange [-3*pi:3*pi]\n");
	fprintf(gnuplotPipe, "set yrange [-1.5:1.5]\n");
	fprintf(gnuplotPipe, "set xtics ('-3π' -3*pi, '-2π' -2*pi, '-π' -pi, '0' 0, 'π' pi, '2π' 2*pi, '3π' 3*pi)\n");
	fprintf(gnuplotPipe, "plot 'Square.dat' with lines linewidth 2 title 'Fourier Approximation'\n");

	pclose(gnuplotPipe);

	return 0;
}
