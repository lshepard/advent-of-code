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

# just swap out a and b direct
dnums2 = dict()
for key, rules in dnums.items():
    rules2 = []
    for rule in rules:
        rule2 = []
        for term in rule.split(" "):
            if term == "16":
                term = "b"
            elif term == "26":
                term = "a"
            rule2.append(term)
        rules2.append(" ".join(rule2))
    dnums2[key] = rules2
dnums = dnums2

strings = inp[i:]

# put them in a trie
t = pygtrie.CharTrie()
for s in strings:
    t[s] = True

def num_that_match(items, possible_strings):
    global t
#    print(" ".join([str(i) for i in items]))


    has_only_ab = True
    for i, item in enumerate(items):
        if item not in ["a","b"]:
            has_only_ab = False
            if i > 0 and not t.has_subtrie("".join(items[:i])):
                #print("prune ", "".join(items[:i]))
                return 0 # this path is out
            break
            
    if has_only_ab:
        test_string = "".join(items)
        #print("test",test_string)
        if test_string in possible_strings:
            print("found",test_string)
            return 1
        else:
            return 0
    
    s = 0
    for i, item in enumerate(items):
        if item not in ["a","b"]:
            # check that this still a viable path
            
            #print("expand out " + str(item))
            # expand out and see if it matches any of the strings
            matches = dnums.get(int(item))
            if matches:
                for match in matches:
                    st = items[:i] + match.split(" ") + items[i+1:]
                    
                    #print(st)
                    s += num_that_match(st, possible_strings)
    return s

    

# let's try it a different way - generate all the possible permutations and see if they apply to any of the strings


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

# beginning with 0 start expanding
print(num_that_match([0], set(strings)))



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
