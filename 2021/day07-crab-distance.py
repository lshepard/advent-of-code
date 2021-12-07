import fileinput
from bisect import bisect_left

def sum_of_numbers(n):
    return (n / 2) * (1 + n)
    
def cheapest_cost(inp, cost_fn):
    crabs = [int(n) for n in inp.split(",")]
    position_costs = dict((position, cost_fn(crabs, position)) for position in range(min(crabs), max(crabs)))
    min_position = min(position_costs, key=position_costs.get)
    return position_costs[min_position]

def one_cost(crabs, end_position):
    return sum([ abs(crab - end_position) for crab in crabs])

def higher_cost(crabs, end_position):
    return sum([ sum_of_numbers(abs(crab - end_position)) for crab in crabs])

assert(cheapest_cost("16,1,2,0,4,2,7,1,2,14", one_cost) == 37)
assert(cheapest_cost("16,1,2,0,4,2,7,1,2,14", higher_cost) == 168)

crabs = fileinput.input()[0].strip()
print("Part 1")
print(cheapest_cost(crabs, one_cost))

print("Part 2")
print(cheapest_cost(crabs, higher_cost))
