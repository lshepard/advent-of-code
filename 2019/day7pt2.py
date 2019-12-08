from intcode import IntCodeComputer
import numpy as np
from itertools import permutations

def try_phase_sequence(program, phase_sequence):
    v = 0

    computers = [IntCodeComputer(program, phase_setting=phase_sequence[i]) for i in range(5)]
        
    last_value = 0

    c1 = computers[0]
    c2 = computers[1]
    c3 = computers[2]
    c4 = computers[3]
    c5 = computers[4]

    ci = 0
    
    
    while True:
        if ci == 0:
            c = c1
        elif ci == 1:
            c = c2
        elif ci == 2:
            c = c3
        elif ci == 3:
            c = c4
        elif ci == 4:
            c = c5
            
        print(f"adding input {last_value} {c.isdone()}")
        c.add_input(last_value)
        last_value = c.compute()
        
        if (c1.isdone() and c2.isdone() and c3.isdone() and c4.isdone() and c5.isdone()):
            return last_value

        ci = (ci + 1) % 5
    
#    return last_value

def phase_sequences(min, max):
    return ["".join([str(c) for c in l]) for l in permutations(range(min,max+1))]

def max_phase_sequence(program):

#    phase_sequences = [np.base_repr(i, base=5) for i in range(3125)]
    sequences = phase_sequences(5,9)
    results = {s: int(try_phase_sequence(program, list(s))) for s in sequences}

    maxsequence = max(results, key=results.get)

    return (maxsequence, results[maxsequence])

def run_tests():

    assert(try_phase_sequence("3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5", "98765") == "139629729")
    assert(max_phase_sequence("3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5")== ("98765",139629729))

run_tests()
print("Part 1:")
r = open("day7.input").read()
print(max_phase_sequence(r))
