import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-10,11)
y = x**2

plt.plot(x,y,label='Quadratic fxn')
plt.legend()
plt.xlabel('input')
plt.ylabel('output')
plt.show()
