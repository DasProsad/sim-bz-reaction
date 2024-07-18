#!/usr/bin/env python3

import sys
import argparse
import numpy as np
from scipy.signal import convolve2d
import matplotlib.pyplot as plt
from matplotlib import animation

plt.rcParams['text.usetex'] = True
plt.rc("font", family="serif")

def update(p, arr):
	"""
	Update arr[p] to arr[q] by evolving in time.
	"""
	# Count the average amount of each species in the 9 cells around each cell by convolution with the 3x3 array m.
	q = (p + 1) % 2
	s = np.zeros((3, ny, nx))
	m = np.ones((3, 3)) / 9
	for k in range(3):
		s[k] = convolve2d(arr[p, k], m, mode="same", boundary="wrap")

	# Apply the reaction equations
	arr[q, 0] = s[0] + s[0] * (alpha * s[1] - gamma * s[2])
	arr[q, 1] = s[1] + s[1] * (beta * s[2] - alpha * s[0])
	arr[q, 2] = s[2] + s[2] * (gamma * s[0] - beta * s[1])

	# Ensure the species concentrations are kept within [0, 1].
	np.clip(arr[q], 0, 1, arr[q])
	return arr

def animate(i, arr, t):
	"""
	Update the image for iteration i of the Matplotlib animation.
	"""
	arr = update(i % 2, arr)
	im.set_array(arr[i % 2, 0])
	ax.axis("off")
	ax.set_title(f"t = {t[i]:.2f} sec", fontsize = 18)
	return [im]

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Simulate BZ-reaction")
	parser.add_argument("-o", "--option", type=str, required=True, help="Save or play the animation [s|p]")
	parser.add_argument("-t", "--duration", type=int, required=True, help="Duration of the simulation (sec)")
	args = parser.parse_args()

	# Width, height of the image.
	nx, ny = 400, 400

	# Reaction parameters.
	alpha, beta, gamma = 1, 1, 1

	# Initialize the array with random amounts of A, B and C.
	arr = np.random.random(size=(2, 3, ny, nx))

	fps = 30
	
	# Time Array
	t = np.linspace(0, args.duration, int(fps * args.duration))

	fig, ax = plt.subplots()
	im = ax.imshow(arr[0, 0], cmap=plt.cm.magma)
	ax.set_aspect("equal")

	if args.option == "s":
		anim = animation.FuncAnimation(fig, animate, frames=len(t), interval=1000/fps, blit=False, fargs=(arr, t))
		anim.save(filename="bz_sim.mp4", fps=fps)

	elif args.option == "p":
		anim = animation.FuncAnimation(fig, animate, frames=len(t), interval=1000/fps, blit=False, fargs=(arr, t))
		plt.show()

	else:
		print(f"Invalid option {args.option}. Usage: sim_bz.py -o [p|s]")
		sys.exit(1)
