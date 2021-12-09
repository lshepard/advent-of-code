import fileinput
from math import prod

test = """2199943210
3987894921
9856789892
8767896789
9899965678""".split("\n")

def points(lines):
    points = dict()
    for j, row in enumerate(lines):
        for i, point in enumerate(row.strip()):
            points[ (i,j) ] = int(point)
            # check all four directions

    return points

def low_points(points):
    """Find the low points"""
    lows = dict()
    for (i,j), point in points.items():
        if (points.get( (i-1,j), 10 ) > point and
            points.get( (i+1 ,j),  10 ) > point and
            points.get( (i  ,j-1), 10 ) > point and
            points.get( (i  ,j+1), 10 ) > point):
            lows[(i,j)] = point
    return lows

def part1(lines):
    return sum([i + 1 for i in low_points(lines).values()])

def find_basin_points(points, this_p, previous_ps):
    """Given point p, finds the size of the basin that is next to it. Don't bother with previous_p."""
    #print(f"this_p {this_p} previous {previous_ps}")
    if points.get(this_p, 9) == 9:
#        print(f"     stopped {this_p}")
        return []
    else:
        #print(f"           found one at {this_p}")
        next_points = [(this_p[0] + 1, this_p[1]),
                       (this_p[0] - 1, this_p[1]),
                       (this_p[0]    , this_p[1] + 1),
                       (this_p[0]    , this_p[1] - 1)]
        
        next_points = [p for p in next_points if p in points and p not in previous_ps ]
        previous_ps.update([this_p])
        new_points = set([this_p])
        for next_p in next_points:
            new_points.update(find_basin_points(points, next_p, previous_ps))
            previous_ps.update(new_points) # dont rehash previous ground on new iterations
        return new_points
        
def find_basins(points):
    """Find the low points"""
    
    lows = low_points(points)

    # for each low, let's find the size of the basin
    # seems like a recursive function

    basins = dict()
    for low_point in lows.keys():
#        print(f"Finding basin for {low_point}")
        basins[low_point] = find_basin_points(points, low_point, set())
    return basins

def part2(points):
    """three largest basin sizes multiplied together"""
    basins = find_basins(points)
    print(basins)
    print(dict( (k, len(v)) for k, v in basins.items() ))
    return prod(sorted([len(basin) for basin in basins.values()])[-3:])
    
assert(part1(points(test)) == 15)

inp = list(fileinput.input())
print(part1(points(inp)))

assert(part2(points(test)) == 1134)
print(part2(points(inp)))

