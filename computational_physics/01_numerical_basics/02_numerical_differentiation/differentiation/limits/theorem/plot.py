import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("data.txt")

i = data[:,0]
exact_val = data[:,1]
analy_val = data[:,2]
error = data[:,3]

plt.plot(i, error)
plt.xlabel('Power of 10')
plt.ylabel('Error in derivative value')
plt.title('Limit theorem')
plt.show()
