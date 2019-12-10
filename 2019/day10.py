import numpy as np

def build_cells(inpt):
    cells = set()
    for i, row in enumerate(inpt.split("\n")):
        for j, char in enumerate(row):
            if char == "#" or char == "X":
                cells.add((j, i))
    return cells

def most_asteroids(cells):
    d = cell_distances(cells)
    return max(d.values(), key = lambda v : len(v))

def part1(inpt):
    cells = build_cells(inpt)
    return most_asteroids(cells)

def part2(inpt):
    cells = build_cells(inpt)
    vc = viewable_cells(cells)
    origin = max(vc, key=lambda x: len(vc[x]))
    ordered = vaporize_order(cells, origin)
    return ordered[199]
    
def viewable_cells(cells):
    # build the cells
    all_cells = {}
    
    for cell in sorted(cells):
        viewable_cells = set()
        for other_cell in sorted(cells):
            if cell != other_cell:
                intermediate = intermediate_cells(cell, other_cell)
                inter = cells.intersection(intermediate)
 #               print(f"inter between {cell} and {other_cell} = {len(inter) == 0} includes {list(inter)} / {list(intermediate)})")
                if len(inter) == 0:
                    viewable_cells.add(other_cell)
#        print(f"{cell} can view {viewable_cells}")
        all_cells[cell] = viewable_cells
        
    return(all_cells)

def angle(c1, c2):
    raw = np.arctan2(c2[0] - c1[0], -1 * (c2[1] - c1[1]))

    if raw < 0:
        raw += 2*np.pi

    return raw

    
def vaporize_order(cells, origin):

    # for rounds of viewable cells
    # sort by angle from 0

    removed_i = 0
    vaporized_order = []
    cells = cells.copy() # make a copy
    while(len(cells) > 1):
        visible_points = viewable_cells(cells)[origin]
        for c in sorted(visible_points, key=lambda cell: angle(origin, cell)):
            vaporized_order.append(c)
            cells.remove(c)
        
    # go in rounds by detectable asteroids
    return vaporized_order

#return max(cell_distances.values())

def inclusive_range(i1, i2):

    if i1 < i2:
        return range(i1, i2+1)
    else:
        return list(reversed(range(i2, i1+1)))
    
def intermediate_cells(c1, c2):
    """GEnerate all possible intermediatry cells"""
    rx = inclusive_range(c1[0], c2[0])
    ry = inclusive_range(c1[1], c2[1])

    len_y = float(len(ry) - 1)
    len_x = float(len(rx) - 1)
    cells = set()
    for i, x in enumerate(rx):
        for j, y in enumerate(ry):
 #           this_ratio = float(j) / float(i)
            
            if (i > 0 and j > 0) and (len_y / j) == (len_x / i):
#                print(f"adding {x},{y} with i{i} and j{j}")
                cells.add((x, y))
            elif len_y == 0 or len_x == 0:
                cells.add((x, y))

    if c1 in cells:
        cells.remove(c1)
    if c2 in cells:
        cells.remove(c2)
        
    return cells


a0 = """.#..#
.....
#####
....#
...##"""
#assert(most_asteroids(a0) == 8)

a1 = """#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###."""
#assert(most_asteroids(a1) == 35)

a2 = """.#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#.."""
#assert(most_asteroids(a2) == 41)
