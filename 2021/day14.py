import fileinput
from collections import Counter
import re

test = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C""".split("\n")

def part1(lines):

    starter = lines[0].strip()

    maps = dict()
    for line in lines[2:]:
        left, right = line.strip().split(" -> ")

        maps[left] = right
        
    s = starter
    for i in range(40):
        print(f"i {i}")
        insertions = list("." * len(s))
        for l, r in maps.items():
            # keep track of the insertions then do them
            pat = re.compile('(?=(' + l + '))')
            for insertion_point in [m.start() for m in re.finditer(pat, s)]:
                insertions[insertion_point] = r

        ns = ""
        for i, c in enumerate(insertions):
            if c == ".":
                ns += s[i]
            else:
                ns += s[i] + c

        s = ns

    counts = Counter(s)
    print(counts)
    return max(counts.values()) - min(counts.values())
    

#starter, maps, pattern = parse_input(test)
#print(part1(test))
inp = list(fileinput.input())
print(part1(inp))


