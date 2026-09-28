import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

data = np.loadtxt("orbit.dat")

x = data[:,0]
y = data[:,1]

fig, ax = plt.subplots(figsize=(7,7))

ax.set_aspect("equal")

limit = 1.5

ax.set_xlim(-limit, limit)
ax.set_ylim(-limit, limit)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Precessing Orbit")

line, = ax.plot([],[], lw=1)
planet, = ax.plot([],[], "o")

def update(frame):

	end = frame * 100

	if end > len(x):
		end = len(x)

	line.set_data(x[:end], y[:end])

	if end > 0:
		planet.set_data([x[end - 1]], [y[end - 1]])

	return line, planet

animation = FuncAnimation(
	fig,
	update,
	frames=500,
	interval=5,
	blit=True
)

animation.save(
	"precession.gif",
	writer="pillow"
)

print("Ploting Animation....")
plt.show()
