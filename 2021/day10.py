import fileinput

test = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]""".split("\n")

def part1(lines):

    score = 0
    for line in lines:
        corrupt, c = first_corrupt_character(line.strip())
        vals = {
            ')': 3,
            ']': 57,
            '}': 1197,
            '>': 25137
            }
        if corrupt:
            score += vals[c]

    return score

def first_corrupt_character(line):
    pline = ""
    while pline != line:
        print(line)
        # as long as there's no more changes
        pline = line
        line = line.replace("()","").replace("{}","").replace("[]","").replace("<>","")

        invalid_perms = [
            "(}","(]","(>",
            "{)","{]","{>",
            "[)","[}","[>",
            "<)","<}","<]"
        ]
        for perm in invalid_perms:
            if perm in line:
                return (True, perm[1])
            
    return (False, line)
    

def part2(lines):

    inverses = {
        "{" : "}",
        "[" : "]",
        "(" : ")",
        "<" : ">"
        }
    scores = []
    for line in lines:
        corrupt, l = first_corrupt_character(line.strip())
        if not corrupt:
            completion = [inverses[c] for c in reversed(l)]
            scores.append(score(completion))

    return sorted(scores)[int(len(scores)/2)]

def score(completion):
    """Start with a total score of 0. Then, for each character, multiply the total score by 5 and then increase the total score by the point value given for the character in the following table:

): 1 point.
]: 2 points.
}: 3 points.
>: 4 points."""
    score = 0
    scores = {
        ")":1,
        "]":2,
        "}":3,
        ">":4}
    for c in completion:
        score = score * 5
        score += scores[c]
    return score

assert(first_corrupt_character("{([(<{}[<>[]}>{[]{[(<()>") ==(True,'}'))
#assert(first_corrupt_character("[[<[([]))<([[{}[[()]]]") == ')')

assert(part1(test) == 26397)
inp = list(fileinput.input())
#print(part1(inp))
#print(part2(test))
print(part2(inp))

