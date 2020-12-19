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

    dnums[left] = rules

    for rule in rules:
        drules[rule]  = drules.get(rule, set())
        drules[rule].add(left) # this is a dict of sets of lists

lleaders = {rule.split(" ")[0] for rule in drules.keys()}

print(sorted(lleaders))


def message_matches(items:list, recursion_depth = 0, ngrams=None):
    global dnums, drules, lleaders
#    print(recursion_depth, "items", " ".join(items))

    # base case
    if items == ["0"]:
        return True
    
    if len(items) and items[0] not in lleaders:
        return False
    
    for i, item in enumerate(items):
        if item in lleaders: # there are possibly others
            for n in [1,2]:
                ngram = items[i:i+n]
                rule_match_set = drules.get(" ".join(ngram))
                if rule_match_set:
                    for rule_match in rule_match_set:
                        res = message_matches(items[:i] + rule_match.split(" ") + items[i+len(ngram):], recursion_depth + 1, ngrams)
                        if res is True:
                            return True
        else:
            return False                

    return False


# now check that the message matches
c = 0
for line in tqdm(inp[i:]):
    # check if the message matches
    if message_matches(list(line.strip())):
        c += 1

print(c)


# 88 88 43 100 59 19 112 117 46 -- is this one?

# only possibility to reduce would be 88 16

# 88 88 43 100 ... can that become 88 16? in this case 16 is b
# so there's no 88 b
# so that whole left side precludes it from working

# what about the right?


# start from the left. if the left one isn't in there, check the left 2, if they can't be compressed
# check the next 1-2 grams over
# if any of them can't find a match, then it's over - the whole chunk of the tree can be eliminated
# no need to waddle around inside looking
# only if there's a possibility
