import re
import itertools
import numpy as np

inpt = open("day12.input").read()


def max_steps_by_axis(tuples):
    """takes a tuples of values and velocities,
    returns how many steps until they match again.

    Key insight is that the axes rotate independently.
    we will see them all sync up when each of them hits
    their rotation independently, determined by the
    least common multiple of each of the cycle lengths."""
    all_previous_tuples = {}
    
    step = 0
    while True:
        tuples_repr = ";".join([f"({t[0]},{t[1]})" for t in tuples])
        if tuples_repr in all_previous_tuples:
            return (all_previous_tuples[tuples_repr], step)
        
        all_previous_tuples[tuples_repr] = step

        # each tuple has as many above as below pushing on it
        num= len(tuples)
        new_tuples = []
        for i in range(0, num):
            pos, vel = tuples[i]
            
            # i move up by the amount above me
            sums = [np.sign(t[0] - pos) for t in tuples]

#            print(sums)
            new_vel = vel + sum(sums)
            new_pos = pos + new_vel
#            print(f"pos:{pos}, vel:{vel}, i:{i}, npos:{new_pos}, nvel:{new_vel}")
            
            new_tuples.append((new_pos, new_vel))
        tuples = new_tuples
        step += 1
        

def in_scans(inpt):
    p = re.compile("<x=([-0-9]+), y=([-0-9]+), z=([-0-9]+)>")
    axes = []
    for row in inpt.split("\n"):
        x, y, z = re.match(p, row).groups()
        axes.append( Moon(int(x),int(y),int(z),0,0,0))
    return axes

    

sample = """<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>"""

#assert(in_scans(sample) == [ (-1,0,2,0,0,0), (2,-10,-7,0,0,0), (4,-8,8,0,0,0), (3,5,-1,0,0,0) ])

input = """<x=-3, y=10, z=-1>
<x=-12, y=-10, z=-5>
<x=-9, y=0, z=10>
<x=7, y=-5, z=-3>"""

def day12pt2(inpt):
    moons = in_scans(inpt)

    axis_x = [ ( moon.x, moon.vx ) for moon in moons]
    axis_y = [ ( moon.y, moon.vy ) for moon in moons]
    axis_z = [ ( moon.z, moon.vz ) for moon in moons]

    max_x =  max_steps_by_axis(axis_x)[1]
    max_y =  max_steps_by_axis(axis_y)[1]
    max_z =  max_steps_by_axis(axis_z)[1]

    return np.lcm.reduce([max_x, max_y, max_z])

print(day12pt2(input))
