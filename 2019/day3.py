



def distance(wire1, wire2):
    x = cells(wire1)
    y = cells(wire2)

#    print(f"x: {sorted(x)}\ny: {sorted(y)}")
    samecells = cells(wire1).intersection( cells(wire2) )
#    print(f"input {wire1} {wire2}")
#    print(samecells)

    return min([abs(cell[0]) + abs(cell[1]) for cell in samecells if cell != (0,0)])

def cells(wire):
    """Returns all cells that the wire touches"""

    x = 0
    y = 0

    points = set()
    
    for direction in wire.split(","):
        dir = direction[0]
        distance = int(direction[1:])
        if dir == "R":
            points.update([(i,y) for i in range(x, x+distance+1)])
            x += distance
        elif dir == "L":
            points.update([(i,y) for i in range(x-distance-1, x)])
            x -= distance
        elif dir == "U":
            points.update([(x,i) for i in range(y, y+distance+1)])
            y += distance
        elif dir == "D":
            points.update([(x,i) for i in range(y-distance-1, y)])
            y -= distance
        else:
            raise Exception("this can't happen " + direction)

    return points
        
x = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
y = "U62,R66,U55,R34,D71,R55,D58,R83"

assert(distance(x,y) == 159)
assert(distance("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51","U98,R91,D20,R16,D67,R40,U7,R15,U6,R7") == 135)
print("passed assertS")
fp = open('day3.input')
inp = fp.readlines()
print(distance(inp[0],inp[1]))

