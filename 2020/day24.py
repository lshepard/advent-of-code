
increments  = {
    "e": (1,0),
    "w": (-1,0),
    "ne": (.5,.5),
    "nw": (-.5,.5),
    "se": (.5, -.5),
    "sw": (-.5, -.5)
}

import re

test = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew"""
def cellval(row):
    directions = re.findall("(se|sw|ne|nw|e|w)", row)

    cell = (0,0)
    
    cell_increments = [increments[direction] for direction in directions]

#    print(cell_increments)
    xs = [float(i[0]) for i in cell_increments]
    ys = [float(i[1]) for i in cell_increments]
    #print(xs)
    
    return (sum(xs),sum(ys))


#print("nwwswee",    cellval("nwwswee"))

lines = open("inputs/day24").readlines()
#lines = test.split("\n")
cells = []
for row in lines:
    cells += [ cellval(row) ]

#print(cells)
flipped = dict()

for cell in cells:
    flipped[cell] = flipped.get(cell, 0)
    flipped[cell] = (flipped[cell] + 1) % 2

print(sum(flipped.values()))


def adjacent_cells(cell):
    x = cell[0]
    y = cell[1]
    return [
        (x-1,y),
        (x+1,y),
        (x-0.5,y+0.5),
        (x-0.5,y-0.5),
        (x+0.5,y+0.5),
        (x+0.5,y-0.5)
        ]


for i in range(100):

    next_turn = flipped.copy()

    for cell, value in flipped.items():
        num_neighbors = sum([flipped.get(neighbor,0) for neighbor in adjacent_cells(cell)])
#        print(f"    {cell}: {value} neighbors {num_neighbors}")
#        for c in sorted(adjacent_cells(cell)):
#            print(f"          {c} {flipped.get(c,'new')}")

        next_val = value # by default stays the same
        if value == 1:
            if (num_neighbors == 0): 
                print(f"flipping {cell} 1 to 0 - zero neighbors")
                next_val = 0
            elif (num_neighbors > 2):
                print(f"flipping {cell} 1 to 0 - 2+ neighbors {num_neighbors}")
                next_val = 0
        elif value == 0:
            if num_neighbors == 2:
                print(f"flipping {cell} 0 to 1")
                next_val = 1
        next_turn[cell] = next_val


        # check the neighbors too
        for n in adjacent_cells(cell):
            if n not in next_turn: # hasn't already been factored
                num_neighbors = sum([flipped.get(neighbor,0) for neighbor in adjacent_cells(n)])
                if num_neighbors == 2:
                    print(f"flipping {n} new neighbor to 1")
                    next_turn[n] = 1 # add it to the cycle
                    
    flipped = next_turn
    print(f"Day {i}: { sum(flipped.values()) }")
    
