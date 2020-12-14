# Bit masking
import re
import fileinput

lines = list(fileinput.input())

mask = ""
mem = dict()
for line in lines:
    print(mem)
    print(line)
    mem_matches = re.match("mem\[(\d+)\] = (\d+)",line)
    mask_matches = re.match("mask = ([01X]+)",line)
    if mem_matches:
        addr = mem_matches[1]
        val = mem_matches[2]

        current = int(val)
        newvalstr = ""
        # work through the mask backwards
        for i, c in enumerate(mask[::-1]):
            current, rem = divmod(current, 2)
            newdigit = rem if (c == "X") else c
            newvalstr = str(newdigit) + newvalstr
            
        mem[addr] = int(newvalstr,2)
            
    elif mask_matches:
        mask = mask_matches[1]
    else:
        raise ValueError("invalid line " + line)
    
print("Part 1")
print(sum(mem.values()))
 
