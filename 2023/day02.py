import math
import re
import fileinput


def parse(line):
    """Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red""" 

    m = re.match("Game (\d+): (.*)", line.strip())
    game_id = int(m[1])

    sets = m[2].split("; ")
    results = []
    for set in sets:
        choices = set.split(", ")

        for c in choices:
            m = re.match("(\d+) (green|red|blue)", c)
            quantity, color = int(m[1]), m[2]
            results.append([quantity, color])

    return game_id, results


def part1():
    """ only 12 red cubes, 13 green cubes, and 14 blue cubes? """
    lines = list(fileinput.input())
    
    n = 0
    for line in lines:
        game_id, set_results = parse(line)
        if possible(set_results, {"red": 12, "green": 13, "blue": 14}):
            print(f"Successful {game_id}")
            n += game_id

    print(n)


def possible(set, comparison):
    """Tells whether the set could work. comparision as form {"green": 2, "red": 3, "blue": 6}"""
    return all([quantity <= comparison[color] for quantity, color in set])

def min_colors_power(set):
    mins = {}

    for (quantity,color) in set:
        mins[color] = max(mins.get(color,0), quantity)
    return math.prod(mins.values())

def part2():
    """ what is the fewest # of cubes of each color that would have made the game possible? """
    lines = list(fileinput.input())
    
    n = 0
    for line in lines:
        game_id, set_results = parse(line)
        p = min_colors_power(set_results)
        print(f"Game {game_id} power {p}")
        n += p

    print(n)

part2()
