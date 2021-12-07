import fileinput

def cheapest_cost(inp):
    crabs = [int(n) for n in inp.split(",")]

    
    
    position_costs = dict((position, cost(crabs, position)) for position in range(min(crabs), max(crabs)))
    print(position_costs)
    min_position = min(position_costs, key=position_costs.get)
    return position_costs[min_position]

def cost(crabs, end_position):
    return sum([ abs(crab - end_position) for crab in crabs])

assert(cheapest_cost("16,1,2,0,4,2,7,1,2,14") == 37)

crabs = fileinput.input()[0].strip()

print(cheapest_cost(crabs))
