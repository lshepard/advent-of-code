
def find_2_sum_to(ints, desired_sum):
    """Part 1"""
    for i in ints:
        for j in ints:
            if (int(i) + int(j)) == desired_sum:
                return int(i) * int(j)

def find_3_sum_to(ints, desired_sum):
    """Obviously this is inefficient, but brute force is pretty easy with this one"""
    for i in ints:
        for j in ints:
            for k in ints:
                if (int(i) + int(j) + int(k)) == desired_sum:
                    return int(i) * int(j) * int(k)

ints = open('inputs/day01').readlines()

print(find_2_sum_to(ints, 2020))
print(find_3_sum_to(ints, 2020))
