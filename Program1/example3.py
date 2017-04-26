from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

from my_functions import sphere_function, ackley_function, accuracy, improvement, convert
from pso import pso

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

domain = 10
# x,y,z = sphere_function(dom=domain)
x,y,z = ackley_function(dom=domain)

opt, init = pso(x, y, z, population_size=20, max_epochs=200)
# global minimum at (0,0,z), where z = ~1.42e-13, which rounds to 0
# global minimum is, in other terms, located at z[100][100], given 200 points per axis between values [-10,10]
print("Accuracy: %.2f%%, Improvement: %.2f%%" % (accuracy(opt[2],search_size=z.max()), improvement(opt[2],init[2],search_size=z.max())))

init_coords = convert(init[0], init[1], search_size=len(z), dom=domain)
opt_coords = convert(opt[0], opt[1], search_size=len(z), dom=domain)

ax.plot_wireframe(x,y,z,rstride=5,cstride=5)
ax.scatter(init_coords[0], init_coords[1], init[2], s=100, c='red')		# initial coordinate
ax.scatter(opt_coords[0], opt_coords[1], opt[2], s=100, c='green')		# final coordinate
plt.show()