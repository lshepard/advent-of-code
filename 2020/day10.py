import math
import itertools

def gaps(nums):
    nums = [int(num.strip()) for num in nums]
    nums.append(max(nums)+3)
    nums.append(0)
    nums = sorted(nums)
    
    gs = []
    for i,n in enumerate(nums):
        if i > 0:
            print(nums[i],nums[i-1])
            gap_size = nums[i] - nums[i-1]
            gs.append(gap_size)
        
    return gs

inp = open("inputs/day10").readlines()
gs  = gaps(inp)
print(gs)
j1 = len([g for g in gs if g == 1])
j3 = len([g for g in gs if g == 3])
print(j1, j3)


print("Part 2")
num_ones = []

bi = 0
for i, n in enumerate(gs):
    if n != 1:
        # stop the list
        num_ones.append(i - bi)
        bi = i +1
num_ones = [n for n in num_ones if n > 0]
print(num_ones)

# choose from a sorted set - which ones

def its(n_ones):
    return sum(range(0,n_ones)) + 1
print("ns")
print(math.prod([its(n) for n in num_ones]))
# 3s and 1s strings
