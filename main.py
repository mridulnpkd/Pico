import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

rows, cols = 6, 6
a, b = 1.0, 1.0  # Unit cell dimensions

# Time control
steps = 200
angle_range = np.linspace(0, np.radians(80), steps)

def generate_vertices(rows, cols, fold_angle):
    verts = np.zeros((rows+1, cols+1, 3))
    for i in range(rows+1):
        for j in range(cols+1):
            x = j * a + (i % 2) * a / 2
            y = i * b * np.sin(fold_angle)
            z = ((-1) ** (i + j)) * b * np.cos(fold_angle)
            verts[i, j] = [x, y, z]
    return verts

def update(frame):
    ax.cla()
    angle = angle_range[frame]
    verts = generate_vertices(rows, cols, angle)

    ax.set_xlim(0, (cols+1) * a)
    ax.set_ylim(0, (rows+1) * b)
    ax.set_zlim(-b, b)
    ax.set_box_aspect([1,1,0.3])
    ax.set_title(f"Fold Angle: {np.degrees(angle):.1f}°")

    # Draw mesh
    for i in range(rows+1):
        ax.plot(verts[i,:,0], verts[i,:,1], verts[i,:,2], 'k')
    for j in range(cols+1):
        ax.plot(verts[:,j,0], verts[:,j,1], verts[:,j,2], 'k')

# Setup plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ani = FuncAnimation(fig, update, frames=steps, interval=50, repeat=True)
plt.show()
