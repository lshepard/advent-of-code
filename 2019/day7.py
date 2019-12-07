from intcode import IntCodeComputer
import numpy as np
from itertools import permutations

def try_phase_sequence(program, phase_sequence):
    v = 0
    
    for phase_setting in phase_sequence:
#        print(f"Trying phase {phase_setting}")
        v = IntCodeComputer(program, inputs=[v, phase_setting]).compute().output()
#        print(f"output is {v}")

    return v

def phase_sequences():
    return ["".join([str(c) for c in l]) for l in permutations([0,1,2,3,4])]

def max_phase_sequence(program):

#    phase_sequences = [np.base_repr(i, base=5) for i in range(3125)]
    print(phase_sequences())
    results = {s: try_phase_sequence(program, list(s)) for s in phase_sequences()}

    print(results)
    maxsequence = max(results, key=results.get)

    return (maxsequence, results[maxsequence])

def run_tests():
    assert(try_phase_sequence("3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0", "43210") == "43210")
    x = max_phase_sequence("3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0")
    assert(x == ("43210", "43210"))
    assert(max_phase_sequence("3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0") == ("01234", "54321"))
    
    assert(max_phase_sequence("3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0") == ("10432", "65210"))

print(max_phase_sequence("3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0"))
#run_tests()
quit()
print("Part 1:")
r = open("day7.input").read()
print(max_phase_sequence(r))
