# Create a square with side length 2r where r = radius of circle
# Randomly place points within square

import numpy as np
import math
import timing
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as mpatches

np.random.seed()

r = 1 # Radius of cricle

def random_point(radius): # Creates a random point within the square of side length 2r
    point = (np.random.rand() * (2 * radius)) - radius # Scales float from 0 -> 1 to -radius -> radius
    return point

def getPi(): # Algorithm for estimating pi
    coords_list = []
    pis = []
    reps = 20000
    in_circle = 0
    out_circle = 0
    for i in range(reps): 
        point_coords = [random_point(r), random_point(r)]
        coords_list.append(point_coords)
        d = math.sqrt(point_coords[0] ** 2 + point_coords[1] ** 2)
        if d <= r:
            in_circle += 1
        else:
            out_circle += 1
        pi_val = 4 * (in_circle / (in_circle + out_circle)) # put this in for loop later to animate. Might have to put its value in coords_list and make it a 3d array to be animated
        pis.append(pi_val) # Adds each pi iteration to a list (for display later)

    point_arr = np.zeros(reps, dtype=[('position', float, 2), ('color', float, 4)])
    coords_arr = np.asarray(coords_list)
    point_arr['position'] = coords_arr

    return point_arr, pis

# Get the array of points and pi values, print the final converged pi 
point_arr, pis = getPi()
print(pis[-1])

# Set axis objects
fig = plt.figure(figsize = (7, 7))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(-1, 1), ax.set_xticks([-1, -.5, 0, .5, 1])
ax.set_ylim(-1, 1), ax.set_yticks([-1, -.5, 0, .5, 1])
ax.set_facecolor('whitesmoke')

# Circle
circ = plt.Circle((0, 0), r, color = 'crimson', fill = False)
ax.add_artist(circ)

# Create scatter
scat = ax.scatter(point_arr['position'][0, 0], point_arr['position'][0, 1], s = 6)

order_format = 1 # Need this for text blitting
def update(current_index): # Animation function. current_index = frame_number 
    point_arr['color'][:current_index] = (np.random.randint(0,256), np.random.randint(0,256), np.random.randint(0,256), 1)
    scat.set_offsets(point_arr['position'][:current_index])
    scat.set_facecolor('steelblue')
    if current_index < len(pis):
        current_pi = pis[current_index]
    
    global order_format

    x = [-.985, -.42, -.42, -.985]
    y = [.94, .94, .985, .985]
    
    if 'current_pi' in locals(): 
        plt.fill([-.985, -.42, -.42, -.985], [.895, .895, .985, .985], 'whitesmoke', zorder = order_format)
        order_format += 1
        ax.text(-.96, .95, 'Pi = {}'.format(current_pi), zorder = order_format)
        ax.text(-.96, .9, 'Points: {}'.format(current_index), zorder = order_format)
        order_format += 1

animation = FuncAnimation(fig, update, interval = 10)
plt.show()

# Math behind pi_val algorithm:
# a_square = 4 * r ** 2
# a_circle = pi * r ** 2
# a_circle / a_square = pi / 4
# 4 (a_circle / a_square) = pi