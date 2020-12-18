import parser
import re

def eval2(formula, nestdepth=0):
    formula = formula.strip()
    print("rewritten", formula, nestdepth)
    
    """ takes a line and rewrites it , rewriting subsequences as well """
    
    # pull out subseqeuences within 
    matches = re.findall(r'\(([^()]+)\)', formula)
    while len(matches) > 0:
        #print(matches, nestdepth)
        for m in matches:
            val = eval2(m)
            formula = formula.replace("("+m+")", str(val)) # replace it in the string
        matches = re.findall(r'\(([^()]+)\)', formula)
    

    # now that there are no nested parens, add the parens inside

    # rewrite the line
    f2 = ""
    c = 0
    for term in formula.split(" "):
        
        if term in ["*","+"]:
            f2 += ")"
            c += 1
        f2 += term + " "

    f2 = "(" * c + f2
    code = parser.expr(f2).compile()
    return eval(code)

#f = "1 + 2 * 3 + 4 * 5 + 6"
f = "2 * 3 + (4 * 5)"
print(eval2(f))
lines = open("inputs/day18").readlines()
#lines = ["1 + (2 * 3) + (4 * (5 + 6))",
#         "2 * 3 + (4 * 5)", "5 + (8 * 3 + 9 + 3 * 4 * 3)",
#         "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) ", "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"]

for line in lines:
    print("orig:",line,"rewrite",eval2(line))
print(sum([int(eval2(line.strip())) for line in lines]))
