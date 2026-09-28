import numpy as np
import matplotlib.pyplot as plt

x_data = np.arange(0,360)
y_data = np.sin(x_data)

plt.plot(x_data,y_data,label='test')
plt.xlabel('input')
plt.ylabel('output')
plt.title('sine curve')
plt.show()
