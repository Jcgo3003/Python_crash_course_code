"""15-3. Molecular Motion: 
Modify rw_visual.py by replacing plt.scatter() with plt.plot(). 
To simulate the path of a pollen grain on the surface of a drop of water, 
pass in the rw.x_values and rw.y_values, and include a linewidth argument. 
Use 5000 instead of 50,000 points."""

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk.
    rw = RandomWalk(1000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))

    point_numbers = range(rw.num_points)

    # Ploting a random walk
    ax.plot(rw.x_values, rw.y_values, linewidth=1)


    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=150)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
        s=150)  

    # Remove the axes. 
    

    plt.show()

    keep_running = input("Make another walk? (y/n): ") 
    if keep_running == 'n':
    	break 