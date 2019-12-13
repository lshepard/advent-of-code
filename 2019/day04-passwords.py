import sys

def program(a,b,comparator):
    c = 0
    for i in range(a,b+1):
        if comparator(i):
#            print(i)
            c += 1

    return c

def meets1(num):
    s = f".{str(num)}."
    rightlen = (len(s) == 8)
    adjacent = any([(s[i] == s[i+1]) for i in range(1,7)])
    increase = ((s[1] <= s[2]) and
                (s[2] <= s[3]) and
                (s[3] <= s[4]) and
                (s[4] <= s[5]) and
                (s[5] <= s[6]))
    return rightlen and adjacent and increase

def meets2(num):
    s = f".{str(num)}."
    rightlen = (len(s) == 8)
    adjacent = any([(s[i] == s[i+1]) and (s[i] != s[i-1]) and (s[i+1] != s[i+2])for i in range(1,7)])
    increase = ((s[1] <= s[2]) and
                (s[2] <= s[3]) and
                (s[3] <= s[4]) and
                (s[4] <= s[5]) and
                (s[5] <= s[6]))
    return rightlen and adjacent and increase

a = int(sys.argv[1])
b = int(sys.argv[2])

assert(meets1(111111))
assert(~meets1(223450))
assert(~meets1(123789))

part1 = program(a,b,meets1)
print(f"Part 1: {part1}")


assert(meets2(112233))
assert(~meets2(123444))
assert(meets2(111122))
assert(~meets2(112232)) # check for increasing order

#145852,616942
part2 = program(a,b,meets2)
print(f"Part 2: {part2}")
