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
        

test = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""


rules = test.split("\n")

assert(parse_rule(rules[0]) == {"light red": {"bright white": 1, "muted yellow": 2}})

#parsed_rules = parse_rules(rules)
#print(parsed_rules)
#assert(part1(parsed_rules) == 4)
print("---")
real = open('inputs/day07').read().strip().split("\n")
pr = parse_rules(real)
#print(pr)
print(part1(pr))
