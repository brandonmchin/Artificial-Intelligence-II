import numpy as np

def circle_function(dom=16.0, delta=0.1):
	x = np.arange(-dom,dom,delta)    # define the x grid
	y = x**2    # calculate function points
	return x,y

def sphere_function(dom=16.0, delta=0.1):
    x = y = np.arange(-dom,dom,delta)    # define the [x,y] grid
    X,Y = np.meshgrid(x,y)    # build all possible points
    Z = X**2 + Y**2    # calculate function points
    return X,Y,Z

def ackley_function(a=20.0, b=0.2, dom=10.0, delta=0.1):
	x = y = np.arange(-dom,dom,delta)    # define the [x,y] grid
	X,Y = np.meshgrid(x,y)    # build all possible points
	Z = a + np.exp(1) - a*np.exp(-b*np.sqrt((X**2+Y**2)/2.0)) - np.exp((np.cos(2.0*np.pi*X)+np.cos(2.0*np.pi*Y))/2)
	return X,Y,Z

###################################################################################################################

def accuracy(result, search_size, goal=0.0):
	# measure how accurate a result is to the goal relative to the search space
	# if len(result) == 2:
	# 	delta = abs(result[0] - goal)
	# else:
	delta = abs(result - goal)
	return 100.0 - ((delta / search_size) * 100.0)

def improvement(final, initial, search_size):
	# measure how well a result improved from its initial position relative to the search space
	# delta = result[1] - result[0]    # delta = initial - final
	delta = initial - final
	return (delta / search_size) * 100

####################################################################################################################

def convert(x, y, search_size, dom):
	# convert [x,y] values back to original cartesian coordinates
	origin = search_size / 2

	if x >= origin:
		new_x = (x * dom * 2 / search_size) - dom
	else:
		new_x = -((origin -x) * dom * 2 / search_size)

	if y >= origin:
		new_y = (y * dom * 2 / search_size) - dom
	else:
		new_y = -((origin -y) * dom * 2 / search_size)

	return new_x, new_y
