from tqdm import tqdm

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

def process_code(code):
    accumulator = 0
    line = 0
    lines_seen = set()
    while(True):
        if line >= len(code):
            #print("hit on the line")
            return accumulator

        if line in lines_seen:
            return None # didn't work

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

#        print(inst, val, accumulator)


def try_changes(code):
    for i, row in tqdm(enumerate(code)):
        r = try_change(code, i)
        if r is not None:
            return r
        
    # going to try each of the changes


def try_change(code, line):
    # change line x of the code and try it out
    #print("changing ",line)
    #print("changing ",code[line])
    inst, val = code[line].split(" ")
    c2 = code.copy()
    if inst == "jmp":
        c2[line] = "nop " + val
        return process_code(c2)
    elif inst == "nop":
        c2[line] = "jmp " + val
        return process_code(c2)
    else:
        return None
    
        
    
#print(process_code(test.split("\n")))

#inp = open('inputs/day07.test').read().strip().split("\n")
inp = open('inputs/day08').readlines()
#print(process_code(inp))

#print(try_changes(test.split("\n")))
print(try_changes(inp))
