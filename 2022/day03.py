import re
import fileinput
import numpy as np

lines = list(fileinput.input())

def shared_type_in_row(row):
    """Given a line from the input, returns the letter of the shared type"""
    half = int(len(row)/2)
    first = row[:half]
    second = row[half:]

    inter = set(list(first)).intersection(set(list(second)))
    if len(inter) != 1:
        raise Exception(f"more or less than 1 intersection in {row}. inter = {inter}")

    return inter.pop()
    
def priority(t):
    """
    Lowercase item types a through z have priorities 1 through 26.
    Uppercase item types A through Z have priorities 27 through 52.
    """
    o = ord(t)
    if o <= 90:
        # uppercase
        a = o - 65 + 27
    else:
        # lowercase
        a = o - 97 + 1
    return a

def pt1():

    total = 0
    for line in lines:
        t = shared_type_in_row(line)
        p = priority(t)
        print(f"{p} ({t})")
        total += p
    return total

def shared_type_in_group(rows):
    """Given a line from the input, returns the letter of the shared type"""
    s = None
    for row in rows:
        rset = set(list(row.strip()))
        if s is None:
            s = rset
        else:
            s = s.intersection(rset)
            
    if len(s) != 1:
        raise Exception(f"more or less than 1 intersection in {row}. inter = {s}")

    return s.pop()

        
def pt2():
    groups = np.array_split(lines, len(lines) / 3)
    total = 0
    for group in groups:
        t = shared_type_in_group(group)
        p = priority(t)
        print(f"{p} ({t})")
        total += p
    return total

print(pt2())
    
