import fileinput
import numpy as np


dirs = {
    "R": (1,0),
    "L": (-1,0),
    "U": (0,1),
    "D": (0,-1)
    }

def next_move(knots,dir_string):
    """Returns the position of the head and tail after the move"""

    direction = dirs[dir_string]
    head = knots[0]
    head = (head[0] + direction[0], head[1] + direction[1])
    new_knots = [ head ]
    
    for i, knot in enumerate(knots[1:]):
        distance = (head[0] - knot[0], head[1] - knot[1])
    
        if abs(distance[0]) <= 1 and abs(distance[1]) <= 1:
            # no change to tail, just return as is
            pass
        else:
            # handles all the changes
            knot = (knot[0] + np.sign(distance[0]), knot[1] + np.sign(distance[1]))

        head = knot # make this the head for the next one
        new_knots.append(knot)

    print(new_knots)
    return new_knots


lines = list(fileinput.input())

def part1():
    H = (0,0)
    T = (0,0)
    tail_spaces = set()
    tail_spaces.add(T)
    
    for line in lines:
        dir_string, num = line.strip().split(" ")
        
        for i in range(int(num)):
            H, T = next_move([H, T], dir_string)
            tail_spaces.add(T)

    return len(tail_spaces)

def part2():
    """Longer tail"""

    knots = [(0,0)] * 10
    tail_spaces = set()
    tail_spaces.add((0,0))

    for line in lines:
        dir_string, num = line.strip().split(" ")
        for i in range(int(num)):
            knots = next_move(knots, dir_string)
            tail_spaces.add(knots[9])
    print(sorted(tail_spaces))
    return len(tail_spaces)


print(f"part 1 : {part1()}")

print(f"part 2 : {part2()}")

