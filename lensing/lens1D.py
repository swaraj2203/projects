import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root

# ============================================================
# TOY QUAD LENS
# ============================================================

# Lens strength
b = 1.0

# Ellipticity-like parameter
q = 1.0


# ------------------------------------------------------------
# Deflection angle
# ------------------------------------------------------------

def alpha(theta):
    """
    Toy elliptical lens deflection.

    theta = [theta_x, theta_y]
    """

    x, y = theta

    # Avoid division by zero
    r = np.sqrt(q**2 * x**2 + y**2)

    if r < 1e-10:
        return np.array([0.0, 0.0])

    alpha_x = b * q * x / r
    alpha_y = b * y / (q * r)

    return np.array([alpha_x, alpha_y])


# ------------------------------------------------------------
# Lens equation
# ------------------------------------------------------------

def lens_equation(theta, beta):
    """
    beta = theta - alpha(theta)

    Returns:
        theta - alpha(theta) - beta
    """

    return theta - alpha(theta) - beta


# ============================================================
# FIND IMAGE POSITIONS
# ============================================================

def find_images(beta, search_range=2.0, n_grid=15):

    solutions = []

    x_values = np.linspace(-search_range, search_range, n_grid)
    y_values = np.linspace(-search_range, search_range, n_grid)

    for x0 in x_values:
        for y0 in y_values:

            result = root(
                lens_equation,
                [x0, y0],
                args=(beta,)
            )

            if result.success:

                theta = result.x

                # Check that solution is actually good
                if np.linalg.norm(
                    lens_equation(theta, beta)
                ) < 1e-6:

                    # Keep only unique solutions
                    if not any(
                        np.linalg.norm(theta - old) < 1e-4
                        for old in solutions
                    ):
                        solutions.append(theta)

    return np.array(solutions)


# ============================================================
# CRITICAL CURVE
# ============================================================

def jacobian(theta):
    """
    Numerical Jacobian of the lens mapping.
    """

    x, y = theta

    eps = 1e-5

    f0 = lens_equation(theta, np.array([0.0, 0.0]))

    fx = lens_equation(
        theta + np.array([eps, 0.0]),
        np.array([0.0, 0.0])
    )

    fy = lens_equation(
        theta + np.array([0.0, eps]),
        np.array([0.0, 0.0])
    )

    J = np.column_stack([
        (fx - f0) / eps,
        (fy - f0) / eps
    ])

    return J


# ------------------------------------------------------------
# Find critical curve numerically
# ------------------------------------------------------------

grid = np.linspace(-2, 2, 500)

X, Y = np.meshgrid(grid, grid)

detA = np.zeros_like(X)

for i in range(len(grid)):
    for j in range(len(grid)):

        theta = np.array([X[i, j], Y[i, j]])

        detA[i, j] = np.linalg.det(jacobian(theta))


# ============================================================
# CHOOSE A SOURCE
# ============================================================

# Try changing these numbers!
beta = np.array([0.0, 0.0])


# Find corresponding images
images = find_images(beta)


# ============================================================
# MAP CRITICAL CURVE TO SOURCE PLANE
# ============================================================

# Extract approximate critical curve using contour
fig_tmp, ax_tmp = plt.subplots()

critical_contour = ax_tmp.contour(
    X,
    Y,
    detA,
    levels=[0]
)

critical_paths = critical_contour.allsegs[0]

plt.close(fig_tmp)


# Map critical curve through lens equation
caustic_paths = []

for path in critical_paths:

    mapped = []

    for point in path:

        mapped_point = point - alpha(point)

        mapped.append(mapped_point)

    caustic_paths.append(
        np.array(mapped)
    )


# ============================================================
# PLOT SOURCE PLANE + LENS PLANE
# ============================================================

fig, (ax_source, ax_lens) = plt.subplots(
    1, 2,
    figsize=(13, 6)
)


# ------------------------------------------------------------
# SOURCE PLANE
# ------------------------------------------------------------

for path in caustic_paths:

    ax_source.plot(
        path[:, 0],
        path[:, 1],
        linewidth=2
    )

# Source
ax_source.scatter(
    beta[0],
    beta[1],
    s=120,
    marker='*',
    zorder=5
)

ax_source.set_xlabel(r'$\beta_x$')
ax_source.set_ylabel(r'$\beta_y$')

ax_source.set_title(
    'SOURCE PLANE'
)

ax_source.set_aspect('equal')
ax_source.grid(alpha=0.25)


# ------------------------------------------------------------
# LENS PLANE
# ------------------------------------------------------------

for path in critical_paths:

    ax_lens.plot(
        path[:, 0],
        path[:, 1],
        linewidth=2
    )

# Lens centre
ax_lens.scatter(
    0,
    0,
    s=60,
    marker='+',
    zorder=5
)

# Images
if len(images) > 0:

    ax_lens.scatter(
        images[:, 0],
        images[:, 1],
        s=100,
        marker='o',
        zorder=5
    )

    # Label images
    for i, image in enumerate(images):

        ax_lens.text(
            image[0] + 0.04,
            image[1] + 0.04,
            f'I{i+1}'
        )

ax_lens.set_xlabel(r'$\theta_x$')
ax_lens.set_ylabel(r'$\theta_y$')

ax_lens.set_title(
    'LENS PLANE'
)

ax_lens.set_aspect('equal')
ax_lens.grid(alpha=0.25)


plt.tight_layout()
plt.show()


# ============================================================
# PRINT IMAGE POSITIONS
# ============================================================

print("Source position:")
print(beta)

print("\nImage positions:")

for i, image in enumerate(images):

    print(
        f"Image {i+1}: "
        f"theta_x = {image[0]:.5f}, "
        f"theta_y = {image[1]:.5f}"
    )
