from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

from my_functions import sphere_function, ackley_function, accuracy, improvement
from sim_annealing import sim_annealing

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x,y,z = sphere_function()
# x,y,z = ackley_function()

opt = sim_annealing(x, y, z)
# global minimum at (0,0,z), where z = ~1.42e-13, which rounds to 0
# global minimum is, in other terms, located at z[100][100], given 200 points per axis between values [-10,10]
print("Accuracy: %.2f%%, Improvement: %.2f%%" % (accuracy(opt, search_size=len(z)), improvement(opt, search_size=len(z))))

ax.plot_wireframe(x,y,z,rstride=5,cstride=5)
plt.show()