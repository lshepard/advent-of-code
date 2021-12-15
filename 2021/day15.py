


from math import ceil
import fileinput
from collections import Counter
import re

test = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581""".split("\n")

def part1(inp):
    """Depth first search through coordinate grid"""

    cells = dict()
    for i, line in enumerate(inp):
        for j, c in enumerate(line.strip()):
            cells[ (i,j) ] = int(c)

    # dynamic programming
    # work our way back from the end. what's the best way to get to the end from each of the surrounding cells

    # sort the cells by distance from the end
    sorted_cells = list(reversed(sorted(cells.keys(), key=lambda x: x[0] + x[1])))

    lowest_risks = dict()
    end_cell = sorted_cells[0] # the last one will be first

    lowest_risks[ end_cell ] = cells[end_cell]
    
    def lowest_risk(start):
#        print(f"evaluating {start}, {path_so_far}")
#        print(f"lowest risks {lowest_risks}")
        if start in lowest_risks:
            return lowest_risks[start]
        
        x, y = start
        adjacent = [ (x + 1, y),
                     (x    , y + 1) ]
        
        risks = [lowest_risk(cell) for cell in adjacent if cell in cells]
        lowest_risks[start] = cells[start] + min(risks)
        return lowest_risks[start]
    
    for cell in sorted_cells[1:]:
        # set the risk
        lowest_risk(cell, [])

    return lowest_risk( (0,0), [] ) - cells[(0,0)]
        # start from the ones closest to the end

def print_cells(cells):

    width = max(cell[0] for cell in cells.keys()) + 1
    height = max(cell[1] for cell in cells.keys()) + 1

    s = ""
    for i in range(width):
        for j in range(height):
            s += str(cells[ (j,i) ])
        s += "\n"
    print(s)
    
def part2(inp):
    """Depth first search through coordinate grid"""

    cells = dict()

    width = len(inp[0].strip())
    height = len(inp)
    print(f"width {width} height {height}")
    for j, line in enumerate(inp):
        for i, c in enumerate(line.strip()):
            # add this in five times
            for x in range(5):
                for y in range(5):
                    cell = (i + x*width, j + y*height)
                    val = (((int(c) + x + y) - 1) % 9 )+ 1
         #           print(cell, c, x, y, val)
                    cells[ cell ] = val

    print_cells(cells)
    # dynamic programming
    # work our way back from the end. what's the best way to get to the end from each of the surrounding cells

    # sort the cells by distance from the end
    sorted_cells = list(reversed(sorted(cells.keys(), key=lambda x: x[0] + x[1])))

    lowest_risks = dict()
    end_cell = sorted_cells[0] # the last one will be first

    lowest_risks[ end_cell ] = cells[end_cell]

    lowest_risk_paths = dict()
    lowest_risk_paths[ end_cell ] = [ end_cell ]
    
    print(end_cell)
    def lowest_risk(start):
        """returns the list with the lowest risk"""
 #       print(start, lowest_risks)
        if start in lowest_risks:
            return lowest_risks[start]
        
        x, y = start
        adjacent = [ (x + 1, y),
                     (x - 1, y),
                     (x    , y + 1),
                     (x    , y - 1) ]
        
        risks = [lowest_risk(cell) for cell in adjacent if cell in cells]
        min_risk = min(risks)
        lowest_risks[start] = cells[start] + min_risk

        lowest_risk_path = [lowest_risk_paths[cell] for cell in adjacent if cell in cells and lowest_risk(cell) == min_risk][-1]
#        print("lowst risk path", lowest_risk_path)
        lowest_risk_paths[start] = [start] + lowest_risk_path

        return lowest_risks[start]
    
    for cell in sorted_cells:
        # set the risk
        lowest_risk(cell)

    print("lowst risk path", lowest_risk_paths[ (0,0) ])
    print("path sum", sum([cells[cell] for cell in lowest_risk_paths[ (0,0) ]]))

        
    return lowest_risk( (0,0) ) - cells[ (0,0) ]
        # start from the ones closest to the end

    

print(part2(test))

inp = list(fileinput.input())
print(part2(inp))
