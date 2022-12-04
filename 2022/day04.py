import re
import fileinput
import numpy as np

lines = list(fileinput.input())



# pt 1
def pair_contains_another(line):
    p1, p2 = line.strip().split(",")
    l1, h1 = [int(x) for x in p1.split("-")]
    l2, h2 = [int(x) for x in p2.split("-")]

    return ( ((l1 <= l2) and (h1 >= h2)) or ((l1 >= l2) and (h1 <= h2)))

# pt 2
def pair_overlaps_at_all(line):
    p1, p2 = line.strip().split(",")
    l1, h1 = [int(x) for x in p1.split("-")]
    l2, h2 = [int(x) for x in p2.split("-")]

    low = max(l1,l2)
    high = min(h1, h2)

    res = (low <= high)
    print(f"{line.strip()} low {low} high {high} - overlaps {res}")
    if res:
        return True
    else:
        return False


total = 0
for line in lines:
    if pair_contains_another(line):
        total += 1

print(f"pt1: {total}")

total = 0
for line in lines:
    if pair_overlaps_at_all(line):
        total += 1

print(f"pt2: {total}")
