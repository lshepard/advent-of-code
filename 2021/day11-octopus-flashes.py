import math
import fileinput

test = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526""".split("\n")

def print_cells(cells, prefix=""):
    s = ""

    x = int(math.sqrt(len(cells)))
    
    for j in range(x):
        s += prefix
        for i in range(x):
            s += str(cells[ (i,j) ])
        s += "\n"
    print(s)
    
def create_cells(lines):
    cells = {}
    print(f"creat cells from {lines}")
    for j, row in enumerate(lines):
        for i, octopus in enumerate(row):
            cells[ (i,j) ] = int(octopus)
    return cells

def part1(cells, num_steps):
    total_flashes = 0
    for i in range(num_steps):
#        print(f"cells {cells}")
        cells, num_flashes = flash(cells)
        total_flashes += num_flashes

    return total_flashes

def part2(cells, num_steps):
    total_flashes = 0
    for i in range(num_steps):
#        print(f"cells {cells}")
        cells, num_flashes = flash(cells)
        if num_flashes == len(cells):
            return i + 1

    return None

def flash(cells):
    """Given a set of cells, return the same number"""
    # first, increment by 1
#    new_cells = dict( (cell, zero_out(value + 1)) for cell, value in cells.items() )

    # BUG: i need to figureo ut how to get the right exact number of flashs in a turn
    # basically, each cell should track the set of surrounding cells that flashed and its original value
    # and then only flash if the count of set exceeds the amount

    flashed_cells = set()

    num_flashed_cells = -1
    while num_flashed_cells != len(flashed_cells): # until things stop changing
        num_flashed_cells = len(flashed_cells)
        # then, check on neighbors
        for cell, value in cells.items():
            # look up how many neighbors have flashed that i know of
            # then look at the time
            flashed_neighbors = [neighbor for neighbor in neighbors(cells, cell) if neighbor in flashed_cells]
            if len(flashed_neighbors) + value + 1 > 9:
                # flash!
                #print(f"Flash! {cell}")
                flashed_cells.add(cell)
#    print_cells(cells)

    new_cells = dict()
    for cell, value in cells.items():
        if cell in flashed_cells:
            new_cells[cell] = 0
        else:
            flashed_neighbors = [neighbor for neighbor in neighbors(cells, cell) if neighbor in flashed_cells]
            new_cells[cell] = len(flashed_neighbors) + value + 1
    print_cells(new_cells)
    
#    cells = dict( (cell, value + 1 + len([neighbor for neighbor in neighbors(cells, cell) if neighbor in flashed_cells]) ) for cell in cells.items() )
    return new_cells, num_flashed_cells
    
def neighbors(cells, cell):
    ns = set()
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            neighbor = (cell[0] + i, cell[1] + j)
            if cells.get(neighbor):
                ns.add(neighbor)
    #print(f"neighbor calculation for cell {cell}. neighbors {sorted(ns)}")
    return ns

t = create_cells("""11111
19991
19191
19991
11111""".split("\n"))
#print(t)
#print(part1(t, 5))

#print(part1(t, 2))

#print(part1(create_cells(test),100))
print(part2(create_cells(test),200))
#print(part1(create_cells(test)))
#print(part1(test))

puzzle_input = """8826876714
3127787238
8182852861
4655371483
3864551365
1878253581
8317422437
1517254266
2621124761
3473331514""".split("\n")
#print(part1(create_cells(puzzle_input),100))
print(part2(create_cells(puzzle_input),5000))
