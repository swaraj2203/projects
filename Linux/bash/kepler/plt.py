import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("orbit.dat")

r = data[:,0]
v = data[:,1]

planets = {
	"Mercury": 0.387,
	"Venus": 0.723,
	"Earth": 1.000,
	"Mars": 1.524,
	"Jupiter": 5.203,
	"Saturn": 9.537,
	"Uranus": 19.19,
	"Neptune": 30.07
}

planet_r = np.array(list(planets.values()))
planet_v = np.sqrt(1.32712440018e20 / (planet_r * 1.495978707e11)) / 1000

plt.figure(figsize=(10,7))
plt.plot(r,v,label=r'$v(r)=\sqrt{\dfrac{GM_\odot}{r}}$')
plt.scatter(planet_r,planet_v,zorder=3)

for name,x,y in zip(planets.keys(),planet_r,planet_v):
	plt.annotate(
		name,
		(x,y),
		xytext=(5, 5),
		textcoords="offset points"
	)

plt.xlabel("Distance from sun [AU]")
plt.ylabel("Orbital velocity [km/s]")
plt.title("Kelplerian Orbital velocity")

plt.grid(True, which="both", alpha=0.3)
plt.legend()

plt.tight_layout()
plt.savefig("Kelperian_curve.png", dpi=300)
plt.show()
