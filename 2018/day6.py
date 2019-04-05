import sys
from collections import Counter

def closest_points(coords):
    coords = [tuple([int(i) for i in c.split(", ")]) for c in coords]
    g = empty_grid(coords)
    h = empty_grid(coords)

    for given in coords:
        for coord in g:
            g[coord][given] = mdist(coord, given)

    for coord, distances in g.items():
        """for each point, what is the set of closest other points?"""
        closest = minimums(distances)
        h[coord] = None if len(closest) > 1 else tuple(closest[0])

    # so i now have, for each coordinate, which of the given set was closest (and None if it was multiples)
    # next up, need to get the sum for each of them
    counts = Counter([closest for (coord, closest) in h.items() if closest is not None])

    edge_coords = {closest for (coord,closest) in h.items() if coord in edges(coords)}
    
    display_board(h)

    print("before",len(counts),counts)
    
#    dict((k,v) for (k,v) in d.items() if k in s)
    without_edges = dict((coord, count) for (coord, count) in counts.items() if coord not in edge_coords)

    print("after",len(without_edges),without_edges)

    # finally disqualify those coordinates that were on the edge (and thus exposed to the "infinite"

    m = max(without_edges, key=without_edges.get)
    return (m, without_edges[m])

def display_board(closest_items):
    closests = {None: '.'}
    base = ord('A') - 1
    
    for (x,y), c in sorted(closest_items.items(), key=lambda a: a[0][1]):
        if x == 0:
            print("")

        if c is None:
            sys.stdout.write(".")
            continue

#        print(c)
        (cx, cy) = c
        if (cx, cy) not in closests:
            base += 1
            closests[c] = chr(base)

        sys.stdout.write(closests[c])
        #else:
        #    sys.stdout.write(closests[c].lower())

    print("\n")
    for c in closests:
        print(c, closests[c])
    
def minimums(some_dict):
    positions = [] # output variable
    min_value = float("inf")
    for k, v in some_dict.items():
        if v == min_value:
            positions.append(k)
        if v < min_value:
            min_value = v
            positions = [] # output variable
            positions.append(k)

    return positions
            
def mdist(c1, c2):
    """Manhattan distance"""
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])
        
def empty_grid(coords):
    (y, x) = zip(*coords)
    all_coords = dict()
    
    for i in range(max(y)+1):
        for j in range(max(x)+1):
            all_coords[(i,j)] = dict()

    return all_coords

def edges(coords):
    (x, y) = zip(*coords)
    max_x = max(x)+1
    max_y = max(y)+1
    
    edge_coords = set()

    for i in range(max_y):
        edge_coords.add((i, 0))
        edge_coords.add((i, max_x))

    for j in range(max_x):
        edge_coords.add((0, j))
        edge_coords.add((0, max_y))
        
    return edge_coords

def safe_region_size(coords):
    """Calculate the size of the safe region that has a total distance
of less than 10000 to all coordinates."""

    # we take the list of for each point the distances to each other one
    # instead of taking the min, we take the sum
    # then we add up how many of those poinst there are, no need for the original coords
    coords = [tuple([int(i) for i in c.split(", ")]) for c in coords]
    g = empty_grid(coords)
    h = empty_grid(coords)

    for given in coords:
        for coord in g:
            g[coord][given] = mdist(coord, given)

    # This was so easy! A one-liner that took a minute after doing the initial calculation
    # Really validates the decision to make a hash of the distances because it was easy to re-use
    return len([coord for (coord, distances) in g.items() if sum(distances.values()) < 10000])

    
    
    
    

if __name__ == "__main__":
    coords = sys.stdin.readlines()
#    print(empty_grid(coords))
#    print(closest_points(coords))
    print(safe_region_size(coords))
    
