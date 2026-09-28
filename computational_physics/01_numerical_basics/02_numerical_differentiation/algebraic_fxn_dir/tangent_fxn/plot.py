import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("tan_data.txt")

x = data[:,0]
y = data[:,1]

y[np.abs(y) > 100] = np.nan

plt.plot(x,y, label='tan fxn')
plt.xlabel('x')
plt.ylabel('tan(x)')
plt.title("Tangent fxn")
plt.legend()
plt.show()
