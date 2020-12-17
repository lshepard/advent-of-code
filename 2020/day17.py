from operator import itemgetter
from itertools import groupby

test = """.#.
..#
###"""

real = """.##...#.
.#.###..
..##.#.#
##...#.#
#..#...#
#..###..
.##.####
..#####."""



def active_cubes(inp):
    cubes = set()
    for x, row in enumerate(inp.split("\n")):
        for y, col in enumerate(list(row)):
            if col == "#":
                cubes.add( ( x, y, 0) )
    return cubes

def print_cubes(cubes):
    scubes = sorted(cubes, key=lambda cube: cube[2])
    for z, cubes in groupby(scubes, key=lambda cube: cube[2]):
        print("z=" + str(z))
        print(sorted(cubes))
    

def next_cubes(cubes):

    all_possible_cubes = set()
    for x,y,z in cubes:
        for a in [x+1,x,x-1]:
            for b in [y+1,y,y-1]:
                for c in [z+1,z,z-1]:
                    all_possible_cubes.add((a,b,c))
    next_cubes = set()
    for x,y,z in all_possible_cubes:
        neighbors = [(a,b,c) for a,b,c in cubes if ( abs(a-x)<=1 and abs(b-y)<=1 and abs(c-z)<=1 and (a!=x or b!=y or c!=z) ) ]
        num_active = len(neighbors)
        # key logic
        
        # If a cube is active and exactly 2 or 3 of its neighbors are also active,
        # the cube remains active. Otherwise, the cube becomes inactive.
        # If a cube is inactive but exactly 3 of its neighbors are active,
        # the cube becomes active. Otherwise, the cube remains inactive.
        active = (num_active == 3) or (num_active == 2 and (x,y,z) in cubes)
#        print(x,y,z,"active",num_active,"isactive",active, neighbors)
        if active:
            next_cubes.add((x,y,z))
            
    return next_cubes
            
def part1(inp):
    cubes = active_cubes(inp)

    for i in range(6):
        print("---- round " + str(i))
        print_cubes(cubes)
#        print(sorted(list(cubes)))
        cubes = next_cubes(cubes)
        # calculate next set of cubes
        
    print(len(cubes))
                
        
part1(real)
