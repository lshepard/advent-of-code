import fileinput
import textwrap
import re

lines = list(fileinput.input())

trees = []

# each of the outsides look in
# build the structure

# go in on each of the directions

height = len(lines)
width = len(lines[0].strip())

# check each tree to see

g = ""
visible_count = 0
for i, line in enumerate(lines):
    print(line.strip())
    for j, tree in enumerate(line.strip()):
        # is it visible from west?
        from_west  = [int(x) for x in line[:j]]
        from_east  = [int(x) for x in line[j+1:width]]

        from_north = [int(lines[x][j]) for x in range(i) ]
        from_south = [int(lines[x][j]) for x in range(i+1,height) ]
        
        v = max(from_west,default=-1)<int(tree) or max(from_east,default=-1)<int(tree) or max(from_north,default=-1)<int(tree) or max(from_south,default=-1)<int(tree)

        
        print(f"visible {v} ({i}, {j}) val {tree} {from_west} {from_east} {from_north} {from_south}")
        if v:
            visible_count += 1
            g += "."
        else:
            g += " "
    g += "\n"

        


print(g)
print(f"visible total: {visible_count}")
