import math
import re
import fileinput
import collections

lines = list(fileinput.input())

part1 = 0
winners = [0] * (len(lines) + 1)
for line in lines:

    m = re.match("Card *(\d+): ([0-9 ]+) \| ([0-9 ]+)", line.strip())

    card_no = m[1]
    winners_cards = [int(x) for x in re.split(" +", m[2]) if len(x) > 0]
    yours = [int(x) for x in re.split(" +", m[3]) if len(x) > 0]
    your_winners = set(winners_cards).intersection(set(yours))
    num_winners = len(your_winners)
    print(card_no)
    winners[int(card_no)] = num_winners
    if num_winners > 0:
        val = 2 ** (len(your_winners) - 1)
    else:
        val = 0
    part1 += val
    #print(f"Card {card_no} has {num_winners} for {val} points. intersect {your_winners}, winners {winners} yours {yours}")

print(f"Part 1: {part1}")

results = [0] * (len(lines) + 1)

# start at the end of the list so we always know the subsequent answers
for card_no in reversed(range(1, len(lines)+1)):
    how_many_winners = winners[card_no]
    results[card_no] = sum(results[card_no + 1: card_no + 1 + how_many_winners]) + 1
    
print(f"Part 2: {sum(results)}")
