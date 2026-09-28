import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("error_acc_data.txt", skiprows=1)

i = data[:,0]
double = data[:,1]
float_ = data[:,2]
double_error = data[:,3]
float_error = data[:,4]

plt.plot(i, double_error, label='double_error')
plt.plot(i, float_error, label='float_error')
plt.title('Error accumulation')
plt.xlabel('Iteration')
plt.ylabel('Error')
plt.legend()
plt.show()

