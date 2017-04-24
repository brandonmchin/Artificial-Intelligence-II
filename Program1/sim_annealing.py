import numpy as np
import random

def acceptance_probability(delta, new_delta, T):
	# acceptance probability > 1 when new_delta is better (higher), thus we always jump
	# 0 < acceptance probability < 1 when new_delta is worse (lower),
	# and we jump only if acceptance probability > random (between 0 and 1)
	# as T approaches 0, the probability of jumping decreases, unless acceptance probability > 1
	return np.exp(-(delta-new_delta)/T)

def calc_move(x, y, z_space):
	# calculate a random new nearby position

    current_z = z_space[x][y]
    option = random.randrange(0,8)    # a random integer between 0 and 7 (8 not included)

    if option == 0:
    	new_pos = [x+1, y]
    	delta = current_z - z_space[x+1][y]
    elif option == 1:
    	new_pos = [x+1, y+1]
    	delta = current_z - z_space[x+1][y+1]
    elif option == 2:
    	new_pos = [x, y+1]
    	delta = current_z - z_space[x][y+1]
    elif option == 3:
    	new_pos = [x-1, y+1]
    	delta = current_z - z_space[x-1][y+1]
    elif option == 4:
    	new_pos = [x-1, y]
    	delta = current_z - z_space[x-1][y]
    elif option == 5:
    	new_pos = [x-1, y-1]
    	delta = current_z - z_space[x-1][y-1]
    elif option == 6:
    	new_pos = [x, y-1]
    	delta = current_z - z_space[x][y-1]
    elif option == 7:
    	new_pos = [x+1, y-1]
    	delta = current_z - z_space[x+1][y-1]

    return new_pos, delta

def sim_annealing(x, y, z, max_evals=100):
	# Given search space (x,y,z), find minimum z by adjusting x and y

	T = 1.0    # temperature
	T_min = 0.00001
	alpha = 0.8    # factor of temperature decrease
	delta = 0.0    # the change between current and new z position

	# Initialize to random starting position within search space
	current_x = random.randrange(0, len(x))
	current_y = random.randrange(0, len(y))

	initial = [current_x, current_y, z[current_x][current_y]]
	print("[%d,%d,%f]" % (current_x, current_y, initial[2]))

	while T > T_min:
		print("Temperature: %f" % T)
		evals = 0
		while evals < max_evals:
			new_pos, new_delta = calc_move(current_x, current_y, z)    # Look for random new nearby position
			ap = acceptance_probability(delta, new_delta, T)

			if ap > random.random():    # jump to new position
				current_x = new_pos[0]
				current_y = new_pos[1]
				delta = new_delta
				print("[%d,%d,%.2f], Delta: %.2f" % (current_x, current_y, z[current_x][current_y], delta))  # print at every jump

			evals = evals + 1

		T = T * alpha

	print("\nFinal: %f" % z[current_x][current_y])

	return z[current_x][current_y], initial[2]