
test = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""


test_fixed = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""

def process_code(code):
    accumulator = 0
    line = 0
    lines_seen = set()
    while(True):
        if line in lines_seen:
            print("Last line " + str(line))
            raise ValueError("last line")
        
        if line >= len(code):
            return accumulator
        lines_seen.add(line)

        inst, val = code[line].split(" ")

        if inst == "acc":
            accumulator += int(val)
            line += 1
        elif inst == "jmp":
            line += int(val)
        elif inst == "nop":
            line += 1
        else:
            raise ValueError("Invalid instruction " + inst)

        print(inst, val, accumulator)


print(process_code(test.split("\n")))

#inp = open('inputs/day07.test').read().strip().split("\n")
inp = open('inputs/day08').readlines()
print(process_code(inp))
