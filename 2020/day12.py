import pytest

def part1(lines):
    x,y = process(lines, wx=1, wy=0, move_on_cardinal_direction=True)
    return abs(x) + abs(y)

def part2(lines):
    x,y = process(lines, wx=10, wy=1, move_on_cardinal_direction=False)
    return abs(x) + abs(y)

def rotate(wx,wy,degrees,direction):
    """Rotates the waypoint N degrees in a direction (either 1 or -1)"""
    for i in range(int(degrees / 90)):
        wy,wx = (-direction * wx), (direction * wy)
    return wx,wy
    
def process(lines, wx, wy, move_on_cardinal_direction):
    x = 0
    y = 0

    for line in lines:
        direction = line.strip()[0]
        val = int(line.strip()[1:])

        dirs = {
            "N": (0,1),
            "S": (0,-1),
            "E": (1,0),
            "W": (-1,0)
            }
        
        if direction == "F":
            x += val * wx
            y += val * wy
        elif direction == "R":
            wx,wy = rotate(wx,wy,val,1)
        elif direction == "L":
            wx,wy = rotate(wx,wy,val,-1)
        elif direction in ["N", "S", "E", "W"]:
            if move_on_cardinal_direction:
                x += val * dirs[direction][0]
                y += val * dirs[direction][1]
            else:
                wx += val * dirs[direction][0]
                wy += val * dirs[direction][1]
        else:
            raise ValueError("invalid line " + line)
        
    return (x,y)

test = ["F10","N3","F7","R90","F11"]

assert part1(test) == 25
assert part2(test) == 286

if __name__ == "__main__":
    inp = open("inputs/day12").readlines()
    
    print("part1")
    print(part1(inp))

    print("part2")
    print(part2(inp))
            
