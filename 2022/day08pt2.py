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

def dscore(trees, this_tree):
    n = 0
    for tree in trees:
        if int(tree) < int(this_tree):
            n += 1
        else:
            return n + 1
    return n

def scenic_score(lines):
    """Find the scenic score for a given row,col"""

    high_score = 0
    g = ""
    for i, line in enumerate(lines):
        for j, tree in enumerate(line.strip()):
            # is it visible from west?
            to_west  = list(reversed([int(x) for x in line[:j]]))
            to_east  = [int(x) for x in line[j+1:width]]
            to_north = list(reversed([int(lines[x][j]) for x in range(i) ]))
            to_south = [int(lines[x][j]) for x in range(i+1,height) ]

            s = dscore(to_west, tree) * dscore(to_east, tree) * dscore(to_north, tree) * dscore(to_south, tree)
            print(f"({i},{j}) [{tree}] score {s} - w{to_west} e{to_east} n{to_north} s{to_south}")
            g = f"{s}\t"
            if s > high_score:
                high_score = s

        g += "\n"
    print(g)
    return high_score

print(scenic_score(lines))
