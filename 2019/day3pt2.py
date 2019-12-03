
def cdist(cell):
    return abs(cell[0]) + abs(cell[1])


def distance(wire1, wire2):
    x = cells(wire1)
    y = cells(wire2)
    
    
    
#    print(f"x: {x}\ny: {y}")
    samecells = set(x.keys()).intersection(set(y.keys()))
#    print(f"samecells: {samecells}")

    costs = {c: x[c] + y[c] for c in samecells if c != (0,0)}
    print(f"costs: {costs}")

    
    
    #    print(f"input {wire1} {wire2}")
    #    print(samecells)
    min_cell = min([c for c in samecells if c != (0,0)], key=lambda c: x[c] + y[c])

    return x[min_cell] + y[min_cell]
    

def cells(wire):
    """Returns all cells that the wire touches"""

    x = 0
    y = 0
    steps = 0
    
    points = dict()
    
    for direction in wire.split(","):
        dir = direction[0]
        distance = int(direction[1:])
        if dir == "R":
            p = [(i,y) for i in range(x+1, x+distance+1)]
            x += distance
        elif dir == "L":
            p = reversed([(i,y) for i in range(x-distance, x)])
            x -= distance
        elif dir == "U":
            p = [(x,i) for i in range(y+1, y+distance+1)]
            y += distance
        elif dir == "D":
            p = reversed([(x,i) for i in range(y-distance, y)])
            y -= distance
        else:
            raise Exception("this can't happen " + direction)

        for point in p:
            steps += 1
            if point not in points:
                points[point] = steps
            
    return points

a = "R8,U5,L5,D3"
b = "U7,R6,D4,L4"

print(distance(a,b))
assert(distance(a,b) == 30)
x = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
y = "U62,R66,U55,R34,D71,R55,D58,R83"
print(distance(x,y))


assert(distance(x,y) == 610)
assert(distance("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51","U98,R91,D20,R16,D67,R40,U7,R15,U6,R7") == 410)
print("passed assertS")
fp = open('day3.input')
inp = fp.readlines()
print(distance(inp[0],inp[1]))

