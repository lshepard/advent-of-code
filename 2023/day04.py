import math
import re
import fileinput
import collections

lines = list(fileinput.input())

part1 = 0
for line in lines:

    m = re.match("Card *(\d+): ([0-9 ]+) \| ([0-9 ]+)", line.strip())

    card_no = m[1]
    winners = [int(x) for x in re.split(" +", m[2]) if len(x) > 0]
    yours = [int(x) for x in re.split(" +", m[3]) if len(x) > 0]

    print(yours)
    your_winners = set(winners).intersection(set(yours))
    num_winners = len(your_winners)
    if num_winners > 0:
        val = 2 ** (len(your_winners) - 1)
    else:
        val = 0
    part1 += val
    print(f"Card {card_no} has {num_winners} for {val} points. intersect {your_winners}, winners {winners} yours {yours}")

print(f"Part 1: {part1}")