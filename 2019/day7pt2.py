from intcode import IntCodeComputer
import numpy as np
from itertools import permutations

def try_phase_sequence(program, phase_sequence):
    v = 0

    computers = [IntCodeComputer(program) for i in range(5)]
    for i, c in enumerate(computers):
        # set initial phase number
        c.add_input(phase_sequence[i])
        
    last_value = 0
    computer_i = 0
    while any([~computer.done for computer in computers]):

        if computers[computer_i].done:
            print(computer)
            print(f"computers: {[not computer.done for computer in computers]}")

        computers[computer_i].add_input(last_value)
        last_value = computers[computer_i].compute()
        computer_i = (computer_i + 1 ) % len(computers)
    
    return last_value

def phase_sequences(min, max):
    return ["".join([str(c) for c in l]) for l in permutations(range(min,max+1))]

def max_phase_sequence(program):

#    phase_sequences = [np.base_repr(i, base=5) for i in range(3125)]
    print(phase_sequences(5,9))
    results = {s: int(try_phase_sequence(program, list(s))) for s in phase_sequences()}

    print(results)
    maxsequence = max(results, key=results.get)

    return (maxsequence, results[maxsequence])

def run_tests():

    assert(try_phase_sequence("3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5", "98765") == 139629729)

run_tests()
print("Part 1:")
#r = open("day7.input").read()
#print(max_phase_sequence(r))
