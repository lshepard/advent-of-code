import re
import fileinput

lines = list(fileinput.input())


nums = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
       "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

revs = dict(("".join(reversed(k)), v)  for k, v in nums.items())

print(revs)
            
def convert_to_nums(txt, regexes):
    """Converts a number like 'abcone2threexyz' to 'abc123xyz'"""

    global rep
    rep = dict((re.escape(k), v) for k, v in regexes.items())
    pattern = re.compile("|".join(rep.keys()))
    x = pattern.sub(lambda m: rep[re.escape(m.group(0))], txt)
    print(txt, x)
    return x

def firstlast(txt):
    """Gets the first/last digit and makes a number"""
    global nums, revs
    
    # left side is easy
    l = re.search("\d",convert_to_nums(txt, nums))[0]
    r = re.search("\d",convert_to_nums("".join(reversed(txt)), revs))[0]

    # for the right one i need to search for the first instance of the phrase from the right
     
    return int(l + r)

nums = [firstlast(line.strip()) for line in lines]

print(len(nums))
print(sum(nums))

    
