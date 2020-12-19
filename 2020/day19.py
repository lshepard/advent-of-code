import re
import pygtrie
from tqdm import tqdm

inp = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b" 

ababbb
bababa
abbbab
aaabbb
aaaabbb
""".split("\n")
inp =  open("inputs/day19").readlines()


# 4 5 4 5 5 5
# 4 3 5 5 5
# 4 3 2 5
# 4 1 5


# ok strategy initially:
# i'll rehash the dict to look up the rule by the reverse




        

dnums = dict()
drules = dict()
for i, line in enumerate(inp):
    if line.strip() == "":
        break
    left, right = line.strip().split(": ")
    
    rules = [r.replace("\"","").strip() for r in right.split("|")]

    dnums[int(left)] = rules

    for rule in rules:
        drules[rule]  = drules.get(rule, set())
        drules[rule].add(left) # this is a dict of sets of lists

# let's just build a regex with this
print(dnums)
def build_regex(item):

    # base state
    if item == "b" or item == "a":
        return item
    
    rules = dnums[int(item)]
    p = "|".join(["".join([build_regex(item) for item in rule.split(" ")]) for rule in rules])
    #    print(p)
    if len(rules) > 1:
        p = "(" + p + ")"

    return p
rest = "^" + build_regex(0) + "$"
print(rest)
r = re.compile(rest)
print(r)
c = 0
for line in inp[i:]:
    if r.match(line.strip()):
        c += 1
    
print(c)
