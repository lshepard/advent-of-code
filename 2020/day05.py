
def seat_id(s):
    s = s.strip()
    fb = s[:7]
    lr = s[-3:]
    row = int(fb.replace("F","0").replace("B","1"),2)
    col = int(lr.replace("L","0").replace("R","1"),2)
    return row*8 +col

assert(seat_id("BFFFBBFRRR") == 567)
assert(seat_id("FFFBBBFRRR") == 119)
assert(seat_id("BBFFBBFRLL") == 820)
assert(seat_id("FBFBBFFRLR") == 357)

real = open('inputs/day05').readlines()

seats = [seat_id(r) for r in real]

print("Part 1", max([seat_id(r) for r in real]))
print("Part 2", ([i for i in range(40,980) if i not in seats]))
