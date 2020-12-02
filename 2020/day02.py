from  collections import Counter

def is_valid(rule):
    print(rule)
    nums, rest = rule.strip().split(" ",1 )
    letter, password = rest.split(":",1)
    lowest, highest = nums.split("-",1)

    c = Counter(list(password))
    count = c.get(letter,0)

    print(letter,lowest,highest,password)
    return (count >= int(lowest)) and (count <= int(highest))

def is_valid2(rule):
    print(rule)
    nums, rest = rule.strip().split(" ",1 )
    letter, password = rest.split(":",1)
    lowest, highest = nums.split("-",1)

    first = password[int(lowest)] == letter
    second = password[int(highest)] == letter

    return (first or second) and not (first and second)

def total_valid(rules):
    return sum([int(is_valid(rule)) for rule in rules])

def total_valid2(rules):
    return sum([int(is_valid2(rule)) for rule in rules])

rules = open('inputs/day02').readlines()

print(total_valid2(rules))
