import re
import fileinput

lines = list(fileinput.input())


def convert_to_nums(txt):
    """Converts a number like 'abcone2threexyz' to 'abc123xyz'"""

    rep = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
           "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    rep = dict((re.escape(k), v) for k, v in rep.items())
    pattern = re.compile("|".join(rep.keys()))
    x = pattern.sub(lambda m: rep[re.escape(m.group(0))], txt)
    print(txt, x)
    return x

def firstlast(txt):
    """Gets the first/last digit and makes a number"""

    l = re.search("\d",txt)[0]
    r = re.search("\d","".join(reversed(txt)))[0]
    print("\t\t", txt,l,r)
    return int(l + r)

nums = [firstlast(convert_to_nums(line.strip())) for line in lines]

print(len(nums))
print(sum(nums))

    
