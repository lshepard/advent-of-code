import re
import pygtrie
from tqdm import tqdm

inp = """0: 8 11
1: "a"
2: 1 24 | 14 4
3: 5 14 | 16 1
4: 1 1
5: 1 14 | 15 1
6: 14 14 | 1 14
7: 14 5 | 1 21
8: 42 | 42 8
9: 14 27 | 1 26
10: 23 14 | 28 1
11: 42 31 | 42 11 31
12: 24 14 | 19 1
13: 14 3 | 1 12
14: "b"
15: 1 | 14
16: 15 1 | 14 14
17: 14 2 | 1 7
18: 15 15
19: 14 1 | 14 14
20: 14 14 | 1 15
21: 14 1 | 1 14
22: 14 14
23: 25 1 | 22 14
24: 14 1
25: 1 1 | 1 14
26: 14 22 | 1 20
27: 1 6 | 14 18
28: 16 1
31: 14 17 | 1 13
42: 9 14 | 10 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba""".split("\n")
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

    if int(item) == 8:# 42 | 42 8
        return "(" + r42 + ")+"
    elif int(item) == 11:
        res = "[z]"
        cur_reg = "" # something that won't hit
        for i in range(12):
            cur_reg = r42 + cur_reg + r31
            res += "|(" + cur_reg + ")"
        ret = "(" + res + ")"
        print("11",ret)
        return ret
    
    p = "|".join(["".join([build_regex(item) for item in rule.split(" ")]) for rule in rules])
    #    print(p)
    if len(rules) > 1:
        p = "(" + p + ")"

    return p

r42 = build_regex(42)
r31 = build_regex(31)
rest = re.compile("^" + build_regex(0) + "$")
print(rest)

c = 0
for line in inp[i:]:
    if re.match(rest, line.strip()):
        print(line.strip())
        c += 1
print(c)

# i could build regex for 42 and 31,
# then do a regex substitution for those on all the strings, and then look by hand?


