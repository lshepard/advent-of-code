import re
import fileinput
import numpy as np
import math

lines = list(fileinput.input())


def parse_input(lines):
    """Create the set of monkeys

    Monkey 0:
      Starting items: 79, 98
      Operation: new = old * 19
      Test: divisible by 23
        If true: throw to monkey 2
        If false: throw to monkey 3
    """

    
    monkeys = []

    monkey = None
    
    for line in lines:
        if m := re.match("Monkey (\d+)", line):
            monkey = {"item_count": 0}
        elif m := re.match(" *Starting items: (.*)", line):
            items = str(m[1]).split(", ")
            monkey["items"] = [int(n) for n in items]
        elif m := re.match(" *Operation: new = old \* old", line):
            # squared
            monkey["op"] = "^"
            monkey["opval"] = 2
        elif m := re.match(" *Operation: new = old ([*-/+]) (\d+)", line):
            monkey["op"] = m[1]
            monkey["opval"] = int(m[2])
        elif m := re.match(" *Test: divisible by (\d+)", line):
            monkey["test"] = int(m[1])
        elif m := re.match(" *If true: throw to monkey (\d+)", line):
            monkey["throwtrue"] = int(m[1])
        elif m := re.match(" *If false: throw to monkey (\d+)", line):
            monkey["throwfalse"] = int(m[1])
        elif line.strip() == "":
            monkeys.append(monkey)
            monkey = None
        else:
            raise Exception(f"Unknown line: {line.strip()}")
    if monkey:
        monkeys.append(monkey)
    return monkeys
            

def do_round(monkeys):
    """Runs a single round, returns the new monkeys"""
    print(f"Starting round with {len(monkeys)} monkeys...")
    for mnum in range(len(monkeys)):
        monkey = monkeys[mnum]
        #print(f"Monkey {mnum}:")

        for item in monkey["items"]:
            #print(f"  Monkey inpsects an item with worry level {item}")
            new = mod_worry(monkey, item)
            new = int(new / 3)
            is_divisible = (new % monkey["test"] == 0)
            target = monkey["throwtrue"] if is_divisible else monkey["throwfalse"]
            #print(f"  Item with worry level {new} is throw to monkey {target}")
            monkeys[target]["items"].append(new)
            monkey["item_count"] += 1
        monkey["items"] = []
        monkeys[mnum] = monkey
    return monkeys
            

def mod_worry(monkey, item):
    o = monkey["op"]
    v = monkey["opval"]
    
    if o == "+":
        return item + v
    elif o == "-":
        return item - v
    elif o == "*":
        return item * v
    elif o == "/":
        return item / v
    elif o == "^":
        return item * item
    else:
        raise Exception(f"bad op code {monkey} {item}")
    

monkeys = parse_input(lines)
for i in range(20):
    monkeys = do_round(monkeys)

item_counts = [monkey["item_count"] for monkey in monkeys]

s = sorted(item_counts, reverse=True)
print(s[0] * s[1])
