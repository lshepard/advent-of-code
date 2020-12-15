from tqdm import tqdm
from compiler.compiler import *
import fileinput

test = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""


test_fixed = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
nop -4
acc +6
"""

    
lines = list(fileinput.input())
c = Compiler(lines)
try:
    c.execute(raise_on_repeat=True)
except RepeatedLineError:
    print("Part 1: " + str(c.accumulator))

print("Part 2 - try all combinations")
for i, line in enumerate(lines):

    inst, val = line.split(" ")
    if inst == "nop":
        line = "jmp " + val
    elif inst == "jmp":
        line = "nop " + val

    clines = lines.copy()
    clines[i] = line
    try:
        print(Compiler(clines).execute(raise_on_repeat=True))
        break
    except RepeatedLineError:
        next
