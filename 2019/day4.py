from operator import itemgetter
from itertools import groupby

def program(a,b):
    """Program for part 1"""

    c = 0
    for i in range(a,b+1):
        if meets(i):
#            print(i)
            c += 1

    return c

def meets(num):
    s = f".{str(num)}."
    rightlen = (len(s) == 8)
    adjacent = any([(s[i] == s[i+1]) and (s[i] != s[i-1]) and (s[i+1] != s[i+2])for i in range(1,7)])
    increase = ((s[1] <= s[2]) and
                (s[2] <= s[3]) and
                (s[3] <= s[4]) and
                (s[4] <= s[5]) and
                (s[5] <= s[6]))
    return rightlen and adjacent and increase


assert(meets(112233))
assert(~meets(123444))
assert(meets(111122))
assert(~meets(112232))

part1 = program(145852,616942)
#part2 = steps(wire1, wire2)
print(part1)
#print(f"Part 1: {part1}")
#print(f"Part 2: {part2}")
