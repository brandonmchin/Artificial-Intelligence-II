import random

def calc_best(x, y, z_space, delta=0):
	# delta equals the change between current and new z position

	current_z = z_space[x][y]
	best = [x,y]    # Initialize optimum to current [x,y] position

	# look in all 8 directions for best nearby point (i.e. highest delta)
	if current_z - z_space[x+1][y] > delta:
		delta = current_z - z_space[x+1][y]
		best = [x+1, y]
	if current_z - z_space[x+1][y+1] > delta:
		delta = current_z - z_space[x+1][y+1]
		best = [x+1,y+1]
	if current_z - z_space[x][y+1] > delta:
		delta = current_z - z_space[x][y+1]
		best = [x,y+1]
	if current_z - z_space[x-1][y+1] > delta:
		delta = current_z - z_space[x-1][y+1]
		best = [x-1,y+1]
	if current_z - z_space[x-1][y] > delta:
		delta = current_z - z_space[x-1][y]
		best = [x-1,y]
	if current_z - z_space[x-1][y-1] > delta:
		delta = current_z - z_space[x-1][y-1]
		best = [x-1,y-1]
	if current_z - z_space[x][y-1] > delta:
		delta = current_z - z_space[x][y-1]
		best = [x,y-1]
	if current_z - z_space[x+1][y-1] > delta:
		delta = current_z - z_space[x+1][y-1]
		best = [x+1,y-1]

	return best, delta

def hill_climbing(x, y, z, max_evals=100):
    # Given search space (x,y,z), find minimum z by adjusting x and y

    # Initialize to random starting position within search space
    current_x = random.randrange(0, len(x))
    current_y = random.randrange(0, len(y))

    print("Initial: [%d,%d], %f" % (current_x, current_y, z[current_x][current_y]))

    evals = 0
    while evals < max_evals:
    	# Continue until either max_evals is reached or local minimum is reached

        best, delta = calc_best(current_x, current_y, z)    # Look for new nearby optimum position

        # Move to nearby optimum position
        current_x = best[0]
        current_y = best[1]

        evals = evals + 1
        print("[%d,%d], Delta: %f" % (current_x, current_y, delta))

        if delta == 0:
            break    # a local minimum was found

    print("Best: %f" % z[current_x][current_y])
    return z[current_x][current_y]