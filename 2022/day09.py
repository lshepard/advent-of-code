import fileinput
import numpy as np

H = (0,0)
T = (0,0)
tail_spaces = set()
tail_spaces.add(T)

dirs = {
    "R": (1,0),
    "L": (-1,0),
    "U": (0,1),
    "D": (0,-1)
    }

def next_move(head,tail,dir_string):
    """Returns the position of the head and tail after the move"""

    direction = dirs[dir_string]
    head = (head[0] + direction[0], head[1] + direction[1])

    distance = (head[0] - tail[0], head[1] - tail[1])

    
    if abs(distance[0]) <= 1 and abs(distance[1]) <= 1:
        # no change to tail, just return as is
        pass
    else:
        # handles all the changes
        tail = (tail[0] + np.sign(distance[0]), tail[1] + np.sign(distance[1]))

    print(f"direction {dir_string} {direction} head {head} tail {tail} distance {distance}")

    return (head, tail)


lines = list(fileinput.input())

for line in lines:
    dir_string, num = line.strip().split(" ")
    
    for i in range(int(num)):
        H, T = next_move(H, T, dir_string)
        tail_spaces.add(T)

print(len(tail_spaces))

