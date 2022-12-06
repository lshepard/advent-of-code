import fileinput
import textwrap
import re

lines = list(fileinput.input())

l =lines[0]

def first_after(l):
    for i in range(len(l) - 14):
        s = set(l[i:i+14])
        print(s)
        if len(s) >= 14:
            return i+14
            
print(first_after(l))
print("finished")
