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


# get the answer
print(strengths)
a = [ strengths[i-1]*i if i<len(strengths) else X for i in desired_strengths ]

print(a)

print(sum(a))
