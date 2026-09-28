import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("quadratic.dat")

x = data[:,0]
y = data[:,1]

plt.plot(x,y,label='Quadratic fxn')
plt.xlabel('input')
plt.ylabel('output')
plt.title(fr'$f(x) = x^2$')
plt.legend()
plt.show()
