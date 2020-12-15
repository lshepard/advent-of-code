# Bit masking
import re
import fileinput

lines = list(fileinput.input())

def part1(lines):
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
    return sum(mem.values())


def part2(lines):
    """Now, we bitmask the mem address instead of bitmasking the values"""
    mask = ""
    mem = dict()
    
    for line in lines:
        print(mem)
        print(line)
        mem_matches = re.match("mem\[(\d+)\] = (\d+)",line)
        mask_matches = re.match("mask = ([01X]+)",line)
        if mem_matches:
            addr = int(mem_matches[1])
            val = int(mem_matches[2])
            current = addr

            addr_str = ""
            # work through the mask backwards
            for i, c in enumerate(mask[::-1]):
                current, rem = divmod(current, 2)

                if c == "0":
                    newdigit = str(rem)
                elif c == "1":
                    newdigit = "1"
                elif c == "X":
                    newdigit = "X"
                else:
                    raise ValueError("unknown c " + c)

                addr_str = newdigit + addr_str
                print(addr_str)
            print(addr_str)
            addrs = mem_addresses(addr_str)
            #print("addrs",addrs)
            for a in addrs:
                an = int(a,2)
                print("writing to " + str(a) + " (" + str(an) + ") val " + str(val))
                mem[an] = val
                
        elif mask_matches:
            mask = mask_matches[1]
        else:
            raise ValueError("invalid line " + line)
    print(mem)
    return sum(mem.values())


def mem_addresses(addr_str, i=0):
#    print("ma", addr_str,i)
    
    if i == len(addr_str):
        return [addr_str]
    else:
        c = addr_str[i]
 #       print("c", c)
        if c != "X":
            return mem_addresses(addr_str, i+1)
        else:
  #          print("expanding")
            return mem_addresses(addr_str[:i] + "1" + addr_str[i+1:], i+1) + \
                   mem_addresses(addr_str[:i] + "0" + addr_str[i+1:], i+1)
        
            
#print(mem_addresses("01X0XX"))
print(part2(lines))
