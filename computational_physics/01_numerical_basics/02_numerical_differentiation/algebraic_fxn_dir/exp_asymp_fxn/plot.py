import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("exp_asympt_data.txt")

x = data[:,0]
x_out = data[:,1]
y = data[:,2]
y_out = data[:,3]
z = data[:,4]
z_out = data[:,5]

z_out[np.abs(z_out)>10] = np.nan

plt.plot(x,x_out, color='firebrick', label='Exponential fxn')
plt.plot(y,y_out, color='green', label='Logarithmic fxn')
plt.plot(z,z_out, color='blue', label='Inverse fxn')
plt.xlabel('x')
plt.ylabel('output')
plt.title('Algebraic functions')
plt.legend()
plt.show()
