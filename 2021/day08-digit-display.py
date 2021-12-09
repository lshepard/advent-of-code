import re
import fileinput
from itertools import permutations

inp = list(fileinput.input())

test = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce""".split("\n")



def how_many_are_easy(inp):
    """How many strings have 2, 4, 3, or 7 characters"""
    n = 0
    
    for line in inp:
        signals, outputs = line.strip().split(" | ")
        for output in outputs.split(" "):
            if len(output) in [2,3,4,7]:
                n += 1

    return n

def part2(inp):
    all_outputs = []
    for line in inp:
        signals, outputs = line.strip().split(" | ")
        wire_mapping = solve_wires(signals.split(" "))
        output = calculate_output(wire_mapping, outputs.split(" "))
        all_outputs.append(output)
    print(all_outputs)
    return sum(all_outputs)

def solve_wires(signals):
    """Given a list of strings, figure out which corresponds to the original"""

    # naively can i go through all permutations
    for perm in permutations("abcdefg"):
        mapping = dict(zip(perm, "abcdefg"))
#        print(f"mapping {mapping} perm {perm}")
        nums = [real_number(mapping, signal) for signal in signals]
        #print(nums)
        if len([num for num in nums if num is None]) == 0:
            print(f"Found a mapping! {mapping}")
            return mapping
    print("no solution found")
    
    
def calculate_output(wire_mapping, outputs):
    """Given the wire mapping, figure out the output"""
    n = ""
    for out in outputs:
        digit = real_number(wire_mapping, out)
        n += str(digit)
        print(f"outputs {out} digit {str(digit)} n {n}")
    return int(n)
    

def real_number(wire_mapping, signal):
    """Given a proposed wire mapping and a signal, return either the number it
    can be - or None if not possible. A wire mapping comes in the form of a 
    7-char string - a correct one would be abcdefg but an alternate may be
    i.e., bacfedg, indicating that b = a, a=b, etc"""
    real_mapping = {
        "abcefg" : 0,
        "cf": 1,
        "acdeg": 2,
        "acdfg": 3,
        "bcdf": 4,
        "abdfg": 5,
        "abdefg": 6,
        "acf": 7,
        "abcdefg": 8,
        "abcdfg": 9
    }

#    print(f"wire mapping {wire_mapping} signal {signal}")
    mapped_signal = "".join(sorted([wire_mapping[c] for c in signal]))
    real = real_mapping.get(mapped_signal)
#    print(f"mapped signal {mapped_signal} real num {real}")
    return real
    

assert(how_many_are_easy(test) == 26)

print("solve wires", solve_wires("acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab".split(" ")))
print(part2(inp))
