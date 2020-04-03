from matplotlib import pyplot as plt
from matplotlib import animation
import math

g = 9.8

def get_intervals(u, theta):

    t_flight = 2*u*math.sin(theta)/g
    intervals = []
    start = 0
    interval = 0.005
    while start < t_flight:
        intervals.append(start)
        start = start + interval
    return intervals

def update_position(i, circle, intervals, u, theta):

    t = intervals[i]
    x = u*math.cos(theta)*t
    y = u*math.sin(theta)*t - 0.5*g*t*t
    circle.center = x, y
    return circle,

def create_animation(u, theta):
    intervals = get_intervals(u, theta)

    xmin = 0
    xmax = u * math.cos(theta) * intervals[-1]
    ymin = 0
    t_max = u * math.sin(theta) / g
    ymax = u * math.sin(theta) * t_max - 0.5 * g * t_max ** 2

    plotmax = max(xmax, ymax)  # Pick the largest dimension of the two
    fig = plt.gcf()

    # Set both maxima to the same value to make a square plot
    ax = plt.axes(xlim=(xmin, plotmax), ylim=(ymin, plotmax))

    # Make sure the two axes are scaled the same...
    #    (we want a circle.. not a messed up oval)
    ax.set_aspect('equal')

    rad = plotmax / 20.  # Make sure the circle doesn't dominate the plot

    circle = plt.Circle((xmin, ymin), rad)  # Use rad instead of 1.0
    ax.add_patch(circle)
    anim = animation.FuncAnimation(fig, update_position,
                                   fargs=(circle, intervals, u, theta),
                                   frames=len(intervals), interval=1,
                                   repeat=False)

    plt.title('Projectile Motion')
    plt.xlabel('X [m]')  # Units are nice :)
    plt.ylabel('Y [m]')
    plt.show()

if __name__ == '__main__':
    try:
        u = float(input('Enter the initial velocity (m/s): '))
        theta = float(input('Enter the angle of projection (degrees): '))
    except ValueError:
        print('You Entered an invalid input')
    else:
        theta = (math.radians(theta))
        create_animation(u, theta)