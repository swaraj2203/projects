import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

data = np.loadtxt("curve.dat")

x = data[:,0]
y = data[:,1]

fig, ax = plt.subplots(figsize=(10,5))

ax.set_xlim(x.min(), x.max())
ax.set_ylim(y.min() * 1.1, y.max() * 1.1)

ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_title("Irregular Damped Oscillation")

line, = ax.plot([],[])

def update(frame):

	end = frame * 20

	if end > len(x):
		end = len(x)

	line.set_data(x[:end], y[:end])

	return line,

animation = FuncAnimation(
	fig,
	update,
	frames = len(x) // 20,
	interval=10,
	blit=True
)

animation.save(
	"curve.gif",
	writer="pillow"
)

plt.show()
