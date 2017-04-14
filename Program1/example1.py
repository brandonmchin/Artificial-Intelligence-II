from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

from my_functions import ackley_function
from hill_climbing import hill_climbing

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x,y,z = ackley_function()

opt = hill_climbing(x, y, z, max_evals=10)
# global minimum at (0,0,z), where z = ~1.42e-13, which rounds to 0
# global minimum is, in other terms, located at z[100][100], given 200 points per axis between values [-10,10]

ax.plot_wireframe(x,y,z,rstride=5,cstride=5)
plt.show()