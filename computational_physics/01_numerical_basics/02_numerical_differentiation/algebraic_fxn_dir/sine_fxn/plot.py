import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("Sine_curve.txt")

x = data[:,0]
y = data[:,1]

plt.plot(x,y,label='sine fxn')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Sine Curve')
plt.legend()
plt.show()
