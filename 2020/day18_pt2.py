import re

def evaluate(expression, r=0):

    # this time, not going to try it recursively
    # we're just going to solve it one term at a time

    while True:
        print(" "*r, expression)
        plus_match = re.search(r"(\d+) \+ (\d+)", expression)
        times_match = re.search(r"(\d+) \* (\d+)", expression)
        parens_match = re.search(r"\(([^()]*)\)", expression)
        if plus_match:
            result = int(plus_match.group(1)) + int(plus_match.group(2))
            start = plus_match.span()[0]
            end = plus_match.span()[1]
            expression = expression[:start] + str(result) + expression[end:]
        elif parens_match:
            result = evaluate(parens_match.group(1), r+1)
            start = parens_match.span()[0]
            end = parens_match.span()[1]
            # -1 and +1 to remove the parentheses that border
            expression = expression[:start] + str(result) + expression[end:]
        elif times_match:
            result = int(times_match.group(1)) * int(times_match.group(2))
            start = times_match.span()[0]
            end = times_match.span()[1]
            expression = expression[:start] + str(result) + expression[end:]
        else:
            return eval(expression)

print(evaluate("3 + (3 * 4)"))

assertions = {
    "1 + (2 * 3) + (4 * (5 + 6)) ": 51,
    "2 * 3 + (4 * 5)": 46,
    "5 + (8 * 3 + 9 + 3 * 4 * 3)": 1445,
    "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))": 669060,
    "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2": 23340
}
for e, res in assertions.items():
    print("evaluatin ", e)
    a =evaluate(e) 
    if a != res:
        raise ValueError("wrong answer for " + e + " : " + str(a) + " should be " + str(res)) 

expressions = open("inputs/day18").readlines()
print("answer", sum([evaluate(e) for e in expressions]))
