from math import ceil
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

def part2(lines):
    starter = lines[0].strip()

    maps = dict()
    for line in lines[2:]:
        left, right = line.strip().split(" -> ")

        maps[left] = [left[0] + right, right + left[1]]

    counts = dict()
    print(f"starter {starter}")
    for i in range(len(starter)-1):
        c = starter[i:i+2]
        counts[c] = counts.get(c, 0) + 1

    # starting counts


    print(counts)
    for i in range(40):
        new_counts = dict()
        for item, count in counts.copy().items():
            r1, r2 = maps[item]
            new_counts[r1] = new_counts.get(r1, 0) + int(count)
            new_counts[r2] = new_counts.get(r2, 0) + int(count)
            
        counts = new_counts
        print(counts)

        single_letter_counts = dict()
        for pair, count in counts.items():
            single_letter_counts[pair[0]] = single_letter_counts.get(pair[0], 0) + count
            single_letter_counts[pair[1]] = single_letter_counts.get(pair[1], 0) + count
            
        print(f"single {single_letter_counts}")

    # final single letter counts
    single_letter_counts = dict()
    for pair, count in counts.items():
        single_letter_counts[pair[0]] = single_letter_counts.get(pair[0], 0) + count
        single_letter_counts[pair[1]] = single_letter_counts.get(pair[1], 0) + count
        

    real_counts = dict( (single, ceil(count / 2)) for single, count in single_letter_counts.items() )

    return max(real_counts.values()) - min(real_counts.values())
    
        
print(part2(test))

inp = list(fileinput.input())
print(part2(inp))


