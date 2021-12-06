import re
import fileinput
import pandas as pd

lines = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010""".split("\n")
lines = list(fileinput.input())

# first calculate the numbers


def mode(nums, position):
    """Calculate the number most prevalent at the position for a set of num strings"""
    total = len(nums)
    one_count = len([num for num in nums if num[position] == "1"])
    print("evaluating for position", position, "ones", one_count, "total" , total, "for nums", nums)
    if one_count >= total/2:
        return "1"
    else:
        return "0"


nums = [line.strip() for line in lines]
print(nums)

def rating(nums, swap_comparison=False):
    for i in range(0,12):
        comparison = mode(nums, i)
        print("position ", i, "comparison", comparison)
        if swap_comparison:
            comparison = str((int(comparison) + 1) % 2)
        swapped = [num for num in nums if num[i] == comparison]
        print(i, swapped)
        if len(swapped) == 1:
            num = swapped[0]
            break
        elif len(swapped) == 0:
            print("last item", nums)
            num = nums[-1]
            break
        nums = swapped
    return int(num,2)

a = rating(nums, False)
b =rating(nums, True)
print (a * b)

#a = num
#print(int(a) * int(b))
