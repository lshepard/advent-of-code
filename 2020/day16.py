import math
import pandas as pd
import fileinput
import re


def parse_lines(lines):
    """Returns the three things: dict of restrictions, your ticket, array of nearby"""

    restrictions = dict()
    yours = None
    nearby = []
    
    for i, line in enumerate(lines):
        if len(line.strip()) == 0:
            break

        key, val = line.split(": ")
        valids = []
        for rule in val.split(" or "):
            mn,mx = rule.split("-")
            valids.extend(list(range(int(mn),int(mx)+1)))
            
        restrictions[key] = valids
        
    yours = lines[i+2].strip().split(",")
    nearby = [line.strip().split(",") for line in lines[i+5:]]

    return restrictions, yours, nearby

lines = open("inputs/day16").readlines()
restrictions, yours, nearby = parse_lines(lines)
#print(restrictions, yours, nearby)
#3print("\n".join(nearby))
#exit

def valid_keys(tnum):
    """gets all the keys that match this num"""
    global restrictions
    return [key for key, valids in restrictions.items() if int(tnum) in valids]

# 
#tnum_valid_keys = dict((tnum, valid_keys(int(tnum))) for tnum in nearby)
#print(tnum_valid_keys)
#invalids = [int(tnum) for tnum in nearby if len(valid_keys(int(tnum))) == 0]
#print(invalids)
#print(sum(invalids))

# part 2
#valids = [int(tnum) for tnum in nearby if len(valid_keys(int(tnum))) > 0]
invalids = set([15, 977, 14, 5, 995, 6, 17, 984, 1, 980, 994, 998, 4, 993, 17, 18, 993, 10, 979, 14, 998, 4, 992, 981, 996, 12, 976, 5, 11, 5, 985, 8, 10, 18, 1, 976, 14, 976, 10, 21, 980, 20, 977, 6, 980, 984, 986, 18, 978, 13, 995, 4])



valid_tickets = [ticket for ticket in nearby if len(set.intersection(set([int(t) for t in ticket]), invalids)) == 0]
print(len(nearby))
print(len(valid_tickets))
# go column by column

available_column_keys = dict()

for i in range(len(nearby[0])): # by columns
    all_valid_keys_for_col = [set(valid_keys(ticket[i])) for ticket in valid_tickets]
    # drop invalid ones
    all_valid_keys_for_col = [k for k in all_valid_keys_for_col if len(k)>0]
    keys = set.intersection(*all_valid_keys_for_col)
    
    available_column_keys[i] = keys


colnum = 0
realized_keys = dict()
while len(available_column_keys) > 0:
    
    if (colnum in available_column_keys) and (len(available_column_keys[colnum]) == 1):
        thekey = available_column_keys[colnum].pop()
        realized_keys[colnum] = thekey
        available_column_keys = dict((k, v-{thekey}) for k, v in available_column_keys.items() if k != colnum)
        print("found " + str(colnum) + " is " + str(thekey))
        colnum = 0
    else:
        colnum += 1


print(realized_keys)

# finally, print hte result

vals = [int(val) for i, val in enumerate(yours) if "departure" in realized_keys[i]]
print(math.prod(vals))
