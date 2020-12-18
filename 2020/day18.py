import parser
import re

def ev(formula):
    print("------ " + formula)
    return eval2(formula)

def replace_pluses(formula):
    """replace the pluses"""
    matches = re.search(r"\d+ \+ \d+", formula)
    if matches is None:
        return eval(formula)
    else:
        formula = formula[:m.start()] + replace_pluses(matches[0]) + formula[m.end():]
    

    
def eval2(formula):
    formula = formula.strip()
    
    """ takes a line and rewrites it , rewriting subsequences as well """
    # if there aren't any parentheses in this ...

    if formula.find("(") == None:
        # then replace all the +s

        
    
    # start by pulling out all the +s
    matches = re.findall(r' (\d+ \+ \d+) ', formula)
    while len(matches) > 0:
#        print(matches)
        for m in matches:
            # just evaluate this one directly
            code = parser.expr(m).compile()
            val = eval(code)

            formula = formula.replace(m, str(val)) # replace it in the string
        matches = re.findall(r' (\d+ \+ \d+) ', formula)
        print(formula)
    
    # pull out subseqeuences within and replace with their values calculated
    matches = re.findall(r'\(([^()]+)\)', formula)
    while len(matches) > 0:
        #print(matches, nestdepth)
        for m in matches:
            val = eval2(m)
            formula = formula.replace("("+m+")", str(val)) # replace it in the string
        matches = re.findall(r'\(([^()]+)\)', formula)
        print(formula)
    # then pull out the addition and do that

    code = parser.expr(formula).compile()
    return eval(code)

#f = "1 + 2 * 3 + 4 * 5 + 6"
f = "2 * 3 + (4 * 5)"
print(eval2(f))
lines = ["1 + 2 * 3 + 4 * 5 + 6 ","1 + (2 * 3) + (4 * (5 + 6))",
         "2 * 3 + (4 * 5)", "5 + (8 * 3 + 9 + 3 * 4 * 3)",
         "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) ", "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"]
lines = open("inputs/day18").readlines()

#for line in lines:
#    print(eval2(line),"orig:",line.strip(),)
    
print("\n".join([str(ev(line.strip())) + "\to:" + line.strip() for line in lines]))
vals = [int(ev(line.strip())) for line in lines]
print(len(vals))
print(sum(vals))
