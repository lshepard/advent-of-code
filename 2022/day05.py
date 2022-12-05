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
    print(f"initial: {initial}, {len(initial[0])}")
    print(f"num_stacks : {num_stacks}")
    stacks = [None] * (num_stacks + 1) # 0'th will be empty
    for i in range(len((stacks))):
        stacks[i] = list()
        
    for line in initial:
        chunks = [line[i:i+4] for i in range(0, len(line), 4)]
        for i, item in enumerate(chunks):
            print(f"'{item}'")
            val = item[1] # 2nd character is the value
            if val.isnumeric():
                pass
            elif val != " ":
                print(f"appending {val}")
                print(f"stacks {stacks}")
                
                stacks[i+1].insert(0,val)
    return stacks


def make_moves(stacks, moves):
    """Make all the given moves to the series of stacks"""

    for move in moves:

        matches = re.match("move (\d+) from (\d+) to (\d+)", move)
        if matches:
            num = int(matches[1])
            frm = int(matches[2])
            to = int(matches[3])

            
            # execute the move
            for i in range(num):
                v = stacks[frm].pop()
                stacks[to].append(v)

    return stacks

def answer(stacks):
    """Takes the top item of each stack into a string"""

    return "".join([stack[-1]  for stack in stacks if len(stack) > 0])

stacks = parse_stacks(initial)
stacks = make_moves(stacks, instructions)
print(answer(stacks))
