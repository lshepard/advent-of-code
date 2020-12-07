import re

def parse_rule(rule):

    left, right = rule.split(" bags contain ")

    right_rules = right.split(", ")
    p = re.compile("([0-9]+) ([a-z ]+) bags?\.?")
    
    if right_rules == ["no other bags."]:
        right_rules = []
        
    rules_dict = {}
    print(right_rules)
    for r in right_rules:
        matches = p.match(r).groups()
        rules_dict[matches[1]] = int(matches[0])
    
    ret = {left: rules_dict}
#    print(ret)
    return ret

def parse_rules(rules):
    prules = {}
    for rule in rules:
        pr = parse_rule(rule)
        print(pr)
        prules.update(pr)
    return prules

def part1(parsed_rules):

    # go through rules and invert them to get a graph traversal

    graph = {}
    for orig, targets in parsed_rules.items():
        for target in targets.keys():
            
            graph[target] = graph.get(target,set())
            graph[target].add(orig)

    print(graph)
    return how_many(graph, "shiny gold")

def how_many(graph, bagtype):
    # need to dedupe these
    print("how many", bagtype)
    if bagtype not in graph:
        return 1
    else:
        return sum([how_many(graph, t) for t in graph[bagtype]])

def part2(parsed_rules):
    print("rules", parsed_rules)
    return how_many2(parsed_rules, "shiny gold") - 1

def how_many2(graph, bagtype):
    s = 1 # one for this bag
    for target_type, num in graph.get(bagtype,[]).items():
        # add all the ones it contains
        s += num * how_many2(graph, target_type)
    return s
#        x = [1 + (int(num) * how_many2(graph, target_type) for (target_type, num) in graph[bagtype].items()]
#        return sum(x)
            

test = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""


test2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""

rules = test2.split("\n")
rules = open('inputs/day07').read().strip().split("\n")
parsed_rules = parse_rules(rules)
print(parsed_rules)
print(part2(parsed_rules))

#
#print(parsed_rules)
#assert(part1(parsed_rules) == 4)
#print("---")
#real = open('inputs/day07').read().strip().split("\n")
#pr = parse_rules(real)
#print(pr)
#print(part1(pr))
