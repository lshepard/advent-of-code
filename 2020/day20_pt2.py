import sys
import re
import math
import fileinput

def read_input():

    correct_orientation = """3389 3461 1327 3719 1877 2801 3761 3853 1009 2113 2963 1621 
3169 2179 3659 3253 3257 1109 3319 2213 1087 2879 2767 3793 
2591 3391 3011 3491 1549 2099 2833 2351 1559 3229 3617 1879 
1511 1607 1217 2251 2887 1231 3187 3581 2011 3313 1907 3709 
1901 1487 1423 2399 1949 1381 2663 1409 1997 1277 3331 1181 
2467 1297 2503 2789 1447 1367 1697 1427 3299 3863 2939 3881 
1777 2609 1303 2543 3821 2137 3889 3733 1789 3623 3527 2593 
1667 3923 2111 3413 1619 2677 1583 2741 3301 2837 2081 1801 
2797 3931 1061 3797 1483 2311 3023 2557 3593 1747 1279 1307 
3449 3697 2441 1051 1319 1579 1489 3271 3163 3191 1091 3541 
2861 3559 2897 1163 1571 3323 1741 1693 1093 1123 2339 3727 
1657 1049 2389 2381 3947 2729 3583 1973 3767 1709 1021 3547 """

    positions = dict()
    co_lines = [line.strip() for line in correct_orientation.split("\n")]
    for j, co_line in enumerate(co_lines):
        for i, tile_num in enumerate(co_line.split(" ")):
#            print(i,j,tile_num)
            positions[int(tile_num)] = (i,j)
            
    tiles = dict()
    for tilestr in open("inputs/day20").read().split("\n\n"):
        lines = tilestr.split("\n")
        tile_num = int(lines[0].split(" ")[1][:-1])
        tiles[ positions[tile_num] ] = "\n".join(lines[1:])

    return tiles

def orient_correctly(tiles):
    """

    Returns a string that represents the tiles all lined up,
    separated by spaces on either side.

    Tile 3389 (top left corner): rotate 1
#.#.#.###.
.........#
#.#.#....#
#.........
#.#.......
..#...#..#
#..#......
#.........
#.#....###
.###.#.###

Tile 3461 (to the right of 3389): rotate 1, flip
#.#.#.###.
#.#......#
##.......#
#..#.##...
..##......
...#....##
#....#....
..#.....##
#...#...##
#.#..##.##

Tile 3169 (below 3389): rotate 1
.#####.#..
#........#
#..#..#..#
...#....#.
.#........
#.#.##..#.
.#........
..........
#....#....
#......##.
"""

    # start at the top left, i know that correct orientation
    # then just move along the line until they are all in the right orientation

    correct = dict()

    
    for j in range (12):
        for i in range (12):
            if (i,j) == (0,0):

                # base case, initial top left needs to rotate once
                correct[(0,0)] = rotate(tiles[( 0,0)])
            else:
                # try different orientations and see if it fits with what's already there
                for rotations in range(4):
                    for flips in range(2):
                        tstring = tiles[(i,j)]
                        for r in range(rotations):
                            tstring = rotate(tstring)
                        if flips == 1:
                            tstring = flip(tstring)
                            
                        # ok , does this work?
                        #print("trying", (i,j), " rotations ", rotations, " flips", flips)
                        #print(tstring)
                        if fits(correct, (i,j), tstring):
                            correct[ (i,j) ] = tstring
                            break
    return correct


def fits(tiles, location, tilestr):
    """Checks if a given tilestr orientation fits at a given location in the tiles array"""
    x, y = location
    
    # look up
    up = tiles.get((x, y-1))
    if up:
        up_last_row = up.split("\n")[-1].strip()
        tile_first_row = tilestr.split("\n")[0].strip()
        if up_last_row != tile_first_row:
            return False
    
    # look down
    down = tiles.get((x, y+1))
    if down:
        down_first_row = down.split("\n")[0].strip()
        tile_last_row = tilestr.split("\n")[-1].strip()
        if down_first_row != tile_last_row:
            return False

    # look left
    left = tiles.get((x-1, y))
    if left:
        left_right_col = [r.strip()[-1] for r in left.split("\n")]
        tile_left_col =  [r.strip()[0] for r in tilestr.split("\n")]
        if left_right_col != tile_left_col:
            return False
        

    # look right
    right = tiles.get((x+1, y))
    if right:
        right_left_col = [r.strip()[0] for r in right.split("\n")]
        tile_right_col =  [r.strip()[-1] for r in tilestr.split("\n")]
        if right_left_col != tile_right_col:
            return False

    return True

def tiles_str(tiles):
    """Prints out a 12x12 grid of tiles, with borders, separated by spaces"""
    s = ""
    for j in range ( 12 * 11 ):
        for i in range ( 12 * 11 ):
            x, x_rem = divmod( i, 11)
            y, y_rem = divmod( j, 11)

            if x_rem == 10 or y_rem == 10:
                c = " "
            else:
                t = tiles.get((x, y))
                if t:
                    # t is a stringblock, with newlines
                    c = t[y_rem * 11 + x_rem]
                else:
                    c = "-"
            s += c
        s += "\n"
    return s

def tiles_str_compact(tiles):
    """Prints out a 12x12 grid of tiles, without borders"""
    s = ""
    for j in range ( 12 * 8 ):
        for i in range ( 12 * 8 ):
            x, x_rem = divmod( i, 8)
            y, y_rem = divmod( j, 8)

            t = tiles.get((x, y))
            if t:
                # tile block is 11 per line (10 + newline)
                # we add 1 to avoid the first row and first col
                c = t[(y_rem+1) * 11 + x_rem+1]
            else:
                c = "-"
            s += c
        s += "\n"
    return s

def rotate(stringblock):
    """Rotates a square block once to the right"""
    lines = [list(row) for row in stringblock.split("\n")]
    length = len(lines)
    return "\n".join(["".join([ lines[length-1-j][i] for j in range(length)]) for i in range(length) ])

def flip(stringblock):
    """Rotates a square block once to the right"""
    lines = [list(row) for row in stringblock.split("\n")]
    length = len(lines)
    return "\n".join(["".join([ lines[i][length-1-j] for j in range(length)]) for i in range(length) ])


def count_dragons_regex(stringblock):
    """Takes a block of characters and counts how many dragons appear."""
    length = len(stringblock.split("\n"))
    line_length=str(length-20+1)
    mask = re.compile("#(..{"+line_length+"})#(....)##(....)##(....)###(.{"+line_length+"}.)#(..)#(..)#(..)#(..)#(..)#", \
                      re.MULTILINE | re.DOTALL)
    replace = r"O\1O\2OO\3OO\4OOO\5O\6O\7O\8O\9O\10O"

    processed, num_dragons = re.subn(mask, replace, stringblock)
    with open("day20.output.image","w") as f:
        f.write(processed)
    
    roughness = processed.count("#")
    
    return num_dragons, roughness


def count_dragons_block(stringblock):
    """
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
"""
    needed_tiles = [
        (0,18),
        (1,0), (1,5), (1,6), (1,11), (1,12), (1,17), (1,18), (1,19),
        (2,1), (2,4), (2,7), (2,10), (2,13), (2,16)
        ]
                
    # look at each block of 3x20
    lines = stringblock.split("\n")
    length = len(lines)
    for j in range(length - 3):
        for i in range(length - 20):
            lineblock = [line[i:i+21] for line in lines[j:j+3]]
            print(i,j)
            print("\n".join(lineblock))
            if all([lineblock[y][x] == "#" for y,x in needed_tiles]):
                print("found at ", (i,j))

tiles = read_input()
tiles = orient_correctly(tiles)

# let's look at the tiles_str oriented correctly
t = tiles_str(tiles).strip()
t = rotate(t)
t = rotate(t)
t = rotate(t)
t = flip(t)
print(t)

s = tiles_str_compact(tiles).strip()
# i believe it's just the one orientation that has them - ignore the others
s = rotate(s)
s = rotate(s)
s = rotate(s)
s = flip(s)


num_dragons, roughness = count_dragons_regex(s)
print(f" yields {num_dragons} dragons {roughness} roughness")

print(count_dragons_block(s))
