import fileinput
import numpy as np
import math

lines = list(fileinput.input())

desired_strengths = [ 20, 60, 100, 140, 180, 220 ]
ans = 1

strengths = []
X = 1

cycle = 0

for i, line in enumerate(lines):

    if line.strip() == "noop":
        strengths.append(X)
    else:
        cmd, val = line.split(" ")
        val = int(val)

        if cmd != "addx":
            raise Exception(f"Incorrect command: {cmd}")

        strengths.append(X)
        strengths.append(X) # do this before
        X += val

# now go through teh strengths

cycle = 0
val = ""
for i in range(6):
    for j in range(40):

        current = strengths[cycle]
        lit = (j in [current-1, current, current+1])

        if lit:
            val += "#"
        else:
            val += "."
        cycle += 1
    val += "\n"
print(val)
            
