import fileinput
import textwrap
import re

lines = list(fileinput.input())

# let's interpret the initial arrangement
instructions = [line for line in lines if ("move" in line)]
initial = lines[:len(lines) - len(instructions) - 1]

def parse_stacks(initial):
    """Create the data structure - a list of lists, to be treated as stacks"""
    num_stacks = int(int(len(initial[0])) / 4)
    stacks = [None] * (num_stacks + 1) # 0'th will be empty
    for i in range(len((stacks))):
        stacks[i] = list()
        
    for line in initial:
        chunks = [line[i:i+4] for i in range(0, len(line), 4)]
        for i, item in enumerate(chunks):
            val = item[1] # 2nd character is the value
            if not val.isnumeric() and val != " ":
                stacks[i+1].insert(0,val)
    return stacks


def make_moves(stacks, moves, keep_order):
    """Make all the given moves to the series of stacks
    keep_order distinguishes part 1 from part 2"""

    for move in moves:

        matches = re.match("move (\d+) from (\d+) to (\d+)", move)
        if matches:
            num = int(matches[1])
            frm = int(matches[2])
            to = int(matches[3])

            if keep_order:
                vals = stacks[frm][-num:]
                stacks[frm] = stacks[frm][:-num]
                stacks[to] += vals
            else:
                for i in range(num):
                    v = stacks[frm].pop()
                    stacks[to].append(v)

    return stacks

def answer(stacks):
    """Takes the top item of each stack into a string"""

    return "".join([stack[-1]  for stack in stacks if len(stack) > 0])


stacks = parse_stacks(initial)
stacks = make_moves(stacks, instructions, keep_order=False)
print(f"pt1: {answer(stacks)}")


stacks = parse_stacks(initial)
stacks = make_moves(stacks, instructions, keep_order=True)
print(f"pt2: {answer(stacks)}")
