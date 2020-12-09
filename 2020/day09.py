from compiler.compiler import *

def part1(nums, preamble_size):
    seen_nums = dict()

    # filled the preamble
    for i in range(preamble_size):
        seen_nums[i] = [nums[i] + nums[j] for j in range(i)]
    
    for i in range(preamble_size,len(nums)):
        # for each one, add the new ones, remove the olds
        del seen_nums[ i - preamble_size]
        seen_nums[i] = [nums[i] + nums[j] for j in range(i-preamble_size+1,i+1)]

        def is_in_group(check_val, seen_nested):
            # now check if it's in the group
            for l in seen_nested:
                for x in l:
                    if x == check_val:
                        return True
            return False
            
        if not is_in_group(nums[i], seen_nums.values()):
            return nums[i]

def part2(nums, desired_sum):
    """Contiguousset of numbers that equals the sum"""
    for i in range(len(nums)):
        # check if it can start at i

        sum = nums[i]
        j = i+1
        while(sum < desired_sum):
            sum += nums[j]
            j += 1

        if sum == desired_sum:
            # hit the answer - find the small and large
            return min(nums[i:j]) + max(nums[i:j])


        
def test_part1():
    nums = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""".split("\n")
    nums = [int(num) for num in nums]
    assert part1(nums, 5) == 127
    
def test_part2():
    nums = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""".split("\n")
    nums = [int(num) for num in nums]
    assert part2(nums, 127) == 62


if __name__ == "__main__":
    nums = open('inputs/day09').readlines()
    nums = [int(num) for num in nums]
    print("part 1")
    v = part1(nums, 25)
    print(v)
    
    print("part 2")
    print(part2(nums, v))
