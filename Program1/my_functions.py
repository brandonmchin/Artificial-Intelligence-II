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
	Z = a + np.exp(1) - a * np.exp(-b * np.sqrt((X**2 + Y**2) / 2.0)) - np.exp((np.cos(2.0 * np.pi * X) + np.cos(2.0 * np.pi * Y)) / 2)
	return X,Y,Z