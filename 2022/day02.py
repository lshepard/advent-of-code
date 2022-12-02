import re
import fileinput

lines = list(fileinput.input())

scores = {
    "A X": 1 + 3,
    "B X": 1 + 0,
    "C X": 1 + 6,
    "A Y": 2 + 6,
    "B Y": 2 + 3,
    "C Y": 2 + 0,
    "A Z": 3 + 0,
    "B Z": 3 + 6,
    "C Z": 3 + 3
    }

# X means lose, Y draw, Z win
pt2scores = {
    "A X": 3 + 0,
    "B X": 1 + 0,
    "C X": 2 + 0,
    "A Y": 1 + 3,
    "B Y": 2 + 3,
    "C Y": 3 + 3,
    "A Z": 2 + 6,
    "B Z": 3 + 6,
    "C Z": 1 + 6
    }

total = 0
for line in lines:
    score = scores[line.strip()]
    total += score

print("pt1: " + str(total))


total = 0
for line in lines:
    score = pt2scores[line.strip()]
    total += score

print("pt2: " + str(total))
