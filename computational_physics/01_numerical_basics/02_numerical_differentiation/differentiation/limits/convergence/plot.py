import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("data.txt")

i  = data[:,0]
h  = data[:,1]
fe = data[:,2]
be = data[:,3]
ce = data[:,4]

plt.plot(i,fe, color="firebrick", alpha=0.7, label="Error with forward difference")
plt.plot(i,be, color="green", alpha=0.7, label="Error with backward difference")
plt.plot(i,ce, color='blue', alpha=0.7, label="Error with central difference")
plt.xlabel("Inverse power of 10")
plt.ylabel("Error")
plt.title("Error in analytical formulae")
plt.legend()
plt.show()
