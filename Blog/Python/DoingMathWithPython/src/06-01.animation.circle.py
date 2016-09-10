from matplotlib import animation
from matplotlib import pyplot as plt

circle = plt.Circle((0,0), 0.05)

def update_radius(i, circle):
    circle.radius = i * 0.5
    return circle

fig = plt.gcf()

ax = plt.axes(xlim=(-10,10), ylim=(-10,10))
ax.set_aspect('equal')
ax.add_patch(circle)

ani = animation.FuncAnimation(fig, update_radius, fargs = (circle,), frames = 30, interval=50)

plt.title('Simple Circle Animation')
plt.show()