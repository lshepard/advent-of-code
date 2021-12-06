from collections import Counter
fish_str = "3,4,3,1,2"
fish_str = "1,1,1,3,3,2,1,1,1,1,1,4,4,1,4,1,4,1,1,4,1,1,1,3,3,2,3,1,2,1,1,1,1,1,1,1,3,4,1,1,4,3,1,2,3,1,1,1,5,2,1,1,1,1,2,1,2,5,2,2,1,1,1,3,1,1,1,4,1,1,1,1,1,3,3,2,1,1,3,1,4,1,2,1,5,1,4,2,1,1,5,1,1,1,1,4,3,1,3,2,1,4,1,1,2,1,4,4,5,1,3,1,1,1,1,2,1,4,4,1,1,1,3,1,5,1,1,1,1,1,3,2,5,1,5,4,1,4,1,3,5,1,2,5,4,3,3,2,4,1,5,1,1,2,4,1,1,1,1,2,4,1,2,5,1,4,1,4,2,5,4,1,1,2,2,4,1,5,1,4,3,3,2,3,1,2,3,1,4,1,1,1,3,5,1,1,1,3,5,1,1,4,1,4,4,1,3,1,1,1,2,3,3,2,5,1,2,1,1,2,2,1,3,4,1,3,5,1,3,4,3,5,1,1,5,1,3,3,2,1,5,1,1,3,1,1,3,1,2,1,3,2,5,1,3,1,1,3,5,1,1,1,1,2,1,2,4,4,4,2,2,3,1,5,1,2,1,3,3,3,4,1,1,5,1,3,2,4,1,5,5,1,4,4,1,4,4,1,1,2"
fish = [int(n) for n in fish_str.split(",")]

def count_fish(fish, num_days):
    """How many fish after num_days?"""

    counts = Counter(fish)
    for i in range(num_days):
        n = sum(counts.values())
        print(f"After {i} days, {n} fish")#: {print_counts(counts)}")
        counts = next_day(counts)
    return n

def print_counts(counts):
    x = ""
    for days_left in sorted(counts.keys()):
        #print(x)
        x += f"{days_left}," * counts[days_left]
    return x
        
def next_day(counts):
    """Gives how many fish will there be the next day"""

    new_counts = dict((k-1, v) for k,v in counts.items())
    time_to_spawn = new_counts.pop(-1,0)
    new_counts[6] = new_counts.get(6,0) + time_to_spawn
    new_counts[8] = time_to_spawn
    return new_counts
    
print(count_fish(fish, 256+1))
