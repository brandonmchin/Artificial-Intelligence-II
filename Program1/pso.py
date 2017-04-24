import numpy as np
import random

class Particle:
	def __init__(self, x, y, z):
		current_x = random.randrange(0, len(x))
		current_y = random.randrange(0, len(y))
		current_z = z[current_x][current_y]
		self.position = [current_x, current_y, current_z]
		self.best = self.position[:]
		self.velocity = random_velocity()

def random_velocity():
	# random integer between -1 and 1 (not including 2)
	x = random.randrange(-1,2)
	y = random.randrange(-1,2)
	return [x,y]

def update_velocity(position, velocity, pbest, gbest):
	c1 = 1
	c2 = 1
	velocity[0] = round(velocity[0] + (c1*random.random()*(pbest[0]-position[0])) + (c2*random.random()*(gbest[0]-position[0])))
	velocity[1] = round(velocity[1] + (c1*random.random()*(pbest[1]-position[1])) + (c2*random.random()*(gbest[1]-position[1])))
	return velocity

def update_position(position, velocity, z_space):
	position[0] = (position[0] + velocity[0]) % len(z_space)	# remain within bounds by using modulo
	position[1] = (position[1] + velocity[1]) % len(z_space)	# remain within bounds by using modulo
	position[2] = z_space[position[0]][position[1]]
	return position

def pso(x, y, z, population_size, max_epochs=100):
	# description

	population = [Particle(x, y, z) for i in range(population_size)]    # initialize particles
	
	best_x = random.randrange(0, len(x))
	best_y = random.randrange(0, len(y))
	best_z = z[best_x][best_y]
	best = [best_x, best_y, best_z]

	initial = best[:]
	print("Initial Global Best: [%d,%d,%f]" % (initial[0], initial[1], initial[2]))

	epochs = 0
	while epochs < max_epochs:
		print("\nEpoch %d" % epochs)
		for i in range(population_size):    # update each particle in population
			population[i].velocity = update_velocity(population[i].position, population[i].velocity, population[i].best, best)
			population[i].position = update_position(population[i].position, population[i].velocity, z)
			if population[i].position[2] <= population[i].best[2]:
				population[i].best = population[i].position[:]
				print("New Personal Best! [%d,%d,%f]" % (population[i].best[0], population[i].best[1], population[i].best[2]))
				if population[i].best[2] <= best[2]:
					best = population[i].best[:]
					print("New Global Best! [%d,%d,%f]" % (best[0], best[1], best[2]))
		epochs = epochs + 1

	return best[2], initial[2]