import math
import re
import fileinput
import collections

lines = list(fileinput.input())

# this will help us avoid out of bounds errors
all_points = set([(x,y) for x in range(len(lines)) for y in range(len(lines[0].strip()))])

part_numbers = []
gears = collections.defaultdict(list)

for row, line in enumerate(lines):
    for m in re.finditer("(\d+)", line.strip()):

        adjacents = [(i,j) for j in range(m.start()-1, m.end()+1) 
                     for i in [row-1,row,row+1] 
                     if i != row or j < m.start() or j >= m.end()]
        
        achars = [lines[i][j] for (i,j) in adjacents if (i,j) in all_points]
        num = int(line[m.start():m.end()])
        is_part_number = len(set(achars) - set(".")) > 0
        if is_part_number:
            part_numbers.append(num)

        # log the gears for next part
        for a in adjacents:
            if (a in all_points) and (lines[a[0]][a[1]] == "*"):
                gears[a].append(num) # defaultdict gives us a list automatically
                
# part1
print(f"Part 1 (sum of part numbers): {sum(part_numbers)}")

# part2
gear_ratios = [math.prod(adjacent_parts) for gear, adjacent_parts in gears.items() if len(adjacent_parts) == 2]
print(f"Part 2 (gear ratios): {sum(gear_ratios)}")
