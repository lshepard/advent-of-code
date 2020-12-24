import sys
import re
import math
import fileinput
SQUARE_SIZE=12
n_tile = 0

class Board():
    """Stores a set of tiles that are matched to each other in a contiguous block.
    Let's start by using a tree structure."""

    def __init__(self, tiles = {}):
        """Intended to be recursive and static, this board calculates things about the board
        and can return a version of itself with a new move if needed"""
        self.tiles = tiles    # key is coordinates, value is the { tile: tile object, permutation : orientation and flipped position of this tile at that location
        self.calculate_open_spaces()

    def __repr__(self):
        # prints the board as it currently stays, with tile ids in each section
        all_coords = self.tiles.keys()
        xs = [c[0] for c in all_coords]
        ys = [c[1] for c in all_coords]

        # display what we can
        
        b = f"Board {len(all_coords)} tiles \n"
        for j in range(min(ys), max(ys) + 1):
            for i in range(min(xs), max(xs) + 1):
                tile = self.tiles.get( (i,j) )

                if tile:
                    b += "{0:4} ".format(tile["tile"].id)
                else:
                    b += "---- "
            b += "\n"

        b += "\n"
        for coords, tile in self.tiles.items():
            perm = str(["{0:010b}".format(n) for n in tile['permutation']])
            b += f"  {coords} \t {tile['tile']} permutation {perm}\n"

        return b

    def image_list(self):
        all_coords = self.tiles.keys()
        xs = [c[0] for c in all_coords]
        ys = [c[1] for c in all_coords]

        x_offset = -min(xs)
        y_offset = -min(ys)

        grid_size = SQUARE_SIZE*8
        
        # init new array - 8 times to capture the lack of border
        newlines = [['/' for x in range(grid_size)] for y in range(grid_size)]

        print(f"length rows:{len(newlines)} cols:{len(newlines[0])}")
        for j in range(min(ys), max(ys) + 1):
            for i in range(min(xs), max(xs) + 1):
                tile = self.tiles.get( (i,j) )

                lines = tile["tile"].inner_repr(tile["permutation"])
                
                for y, line in enumerate(lines):
                    for x, c in enumerate(line):
                        a = (i + x_offset)*8 + x
                        b = (j + y_offset)*8 + y
#                        print(f"ij({i},{j}) ab({a},{b}) Setting {x} + {x_offset}, {y} + {y_offset} to {c}")
                        newlines[b][a] = c
                print( f"\nTile {tile['tile'].id}\n" + "\n".join(["".join(line) for line in lines]))
        
        return "\n".join(["".join(line) for line in newlines])
                        
    
    def corner_tiles(self):
        """Answer to part 1 of the assignment"""
        
        all_coords = self.tiles.keys()
        xs = [c[0] for c in all_coords]
        ys = [c[1] for c in all_coords]
        
        min_x = min(xs)
        min_y = min(ys)
        max_x = max(xs)
        max_y = max(ys)

        return [self.tiles[(x, y)]['tile'].id for x in (min_x, max_x) for y in (min_y, max_y) ]

        
    def get_relative_coords(self, base_coords, direction):
        """Given base coordinates, get the relative tile in this board - or None if none there
        0=top, 1=right, 2=down, 3=left"""
        
        if direction == 0:
            return (base_coords[0], base_coords[1]-1)
        elif direction == 2:
            return (base_coords[0], base_coords[1]+1)
        elif direction == 1:
            return (base_coords[0]+1, base_coords[1])
        elif direction == 3:
            return (base_coords[0]-1, base_coords[1])
                                   
    def calculate_open_spaces(self):
        """Finds all the open spaces for this tile on this board
        format is as a coordinate, direction and value that must be met to fit there"""
        #print("Calculating open spaces ...")
        self.open_spaces = {}

        # each one of these is formatted in nested hash like:
        #  coords -> direction -> value
        for coords, this_tile in self.tiles.items():
         #   print(f"   Calculating open spaces  - {coords} and tile {this_tile}")
            # for each one, look around and see which edges are exposed
            for direction in range(4):
                rel_c = self.get_relative_coords(coords, direction)
          #      print(f"      {rel_c}")

                if not rel_c in self.tiles: # open space - nothing there
                    self.open_spaces[rel_c] = self.open_spaces.get(rel_c, {})

                    # the matching space must be the opposite of the number and the opposite direction
                    # if i'm facing to the left (3) with number N, then i need my matching tile to be facing right (1) with number flip(N)
                    self.open_spaces[rel_c][(direction + 2) % 4] = flip(this_tile['permutation'][direction])
        
    def find_spaces(self, tile):
        """Finds all spaces that will work - returns the space and permutation of the tile that would fit there"""

        open_spaces_for_this_tile = [] # will be a list of tuples, each one containing the coords and permutation
        for coords, space in self.open_spaces.items():

            for permutation in tile.permutations():

                # check each way of fitting against each of the spaces
                if self.fits(coords, permutation):
                    # this will match the current space
                    open_spaces_for_this_tile.append(   (coords, permutation)   )
                    
        return open_spaces_for_this_tile

    def fits(self, coords, permutation):
        space = self.open_spaces.get(coords,{})
        matches = [space[direction] == permutation[direction] for direction in range(4) if direction in space]
        return len(matches) > 0 and all(matches)
        
    def add(self, tile, coords, permutation):
        if self.fits(coords, permutation):
            new_tiles = self.tiles.copy()
            new_tiles[coords] = { "tile" : tile, "permutation": permutation }
            return Board(new_tiles)
        else:
            raise ValueError(f"Cannot add {tile} to {coords} as {permutation}")

            
        

class Tile():

    def __init__(self, tilestr):
        """Parses a "tile". i.e.

        Tile 2939:
        ####...###
        .#....#..#
        ....##....
        ..##......
        .#....#...
        #.....#...
        #.....#...
        ##........
        ......#...
        ##.#.#..#.
        
        Pulls out the id and the four edges."""
        lines = tilestr.split("\n")
        self.tilestr = tilestr
        self.id = int(lines[0].split(" ")[1][:-1])
        
        top_edge =    self.edgenum(lines[1].strip())
        right_edge =  self.edgenum("".join([line[-1] for line in lines[1:] ]))
        bottom_edge = flip(self.edgenum(lines[-1].strip()))
        left_edge =   flip(self.edgenum("".join([line[0] for line in lines[1:] ])))

        self.edges = [top_edge, right_edge, bottom_edge, left_edge]

    def edgenum(self, edgestr):
        """Given an edge, i.e. "##.#.#..#.", converts to a number."""
        return int(edgestr.replace("#","1").replace(".","0"), 2)

    def permutations(self):
        """Gives all eight permutations (rotate, flipped) of these edges"""

        permutations = []
        for n_rotate in range(4):
            for to_flip in [False, True]:
                edges = [self.edges[(i + n_rotate) % len(self.edges)] for i in range(len(self.edges))]
                
                if to_flip: # top to bottom
                    edges = [ flip(edges[2]),
                              flip(edges[1]),
                              flip(edges[0]),
                              flip(edges[3]) ]
                permutations.append(edges)
        return permutations

    def get_rotate_flip_counts(self, permutation):
        """Returns how many times rotation and flip were done for that permuatation"""
        perms = self.permutations()
        for n_rotate in range(4):
            for n_flip in [0, 1]:
                edges = [self.edges[(i + n_rotate) % len(self.edges)] for i in range(len(self.edges))]

                if n_flip:
                    edges = [ flip(edges[2]),
                              flip(edges[1]),
                              flip(edges[0]),
                              flip(edges[3]) ]
                
                if permutation == edges:
                    return (n_rotate, n_flip)

#    def rotate(self, tile):
#        newt = [ tile[10-j,i] for i in range(10) for j in range(10) ]

    def inner_repr(self, permutation):
        """Returns how the inside of the tile looks for a given permutation"""
        (n_rotate, n_flip) = self.get_rotate_flip_counts(permutation)
        global n_tile
        n_tile += 1
        n_tile_ch = chr(n_tile + 65)
        print(f"{n_rotate} rotations and {n_flip} flip repr for {self}")
        lines = [list(r) for r in self.tilestr.split("\n")[1:]]
#        print(lines, len(lines))

        def r(i,j):
            ret=lines[9-i][j]
#            print("rotating", i,j,ret,"to",9-j,i)
#            return n_tile_ch
            return ret
        def f(i,j):
            ret= lines[9-j][i]
#            print("flipping",i,j,ret,"to",i,9-j)
            return ret
        for z in range(n_rotate):
            lines =  [ [r(i,j) for i in range(10)] for j in range(10) ]
        if n_flip:
            lines =  [ [f(i,j) for i in range(10)] for j in range(10) ]

        base_c = 96 if n_tile % 2 == 0  else 64
#        return [[chr(base_c+i+j+n_tile) for i in range(1,9)] for j,line in enumerate(lines[1:9])]
        # now cut off the border
        return [line[1:9] for line in lines[1:9]]
            
    def __repr__(self):
        return "Tile " + str(self.id) + ": " + str(["{0:010b}".format(n) for n in self.edges])

    
def flip(n):
    """Flip an edge"""
    return int("{0:010b}".format(n)[::-1],2)

def solve_puzzle(tiles):

    # for each tile, which other tiles would possibly work?
    # input is only 144 tiles, checking against every other
    # wouldn't be that bad = n^2 = 20k
    
    # first, assemble a hash of tiles that even have a given edge value

    first_tile = tiles[0]
    remaining_tiles = tiles[1:]
    board = Board( tiles = { (0,0) : {
        "tile": first_tile,
        "permutation": first_tile.permutations()[1]}})
    final_board  = completed_board(board,remaining_tiles)
    if not final_board:
        print("Did not reach an answer")
    print(final_board)
    return final_board


def completed_board(board, remaining_tiles):
    """Recursive function to calculate a given board state"""

#    print("\n\n", board)
    
    if len(remaining_tiles) == 0:
        # base case! success!
        return board

    for i, tile in enumerate(remaining_tiles):
        for coords, permutation in board.find_spaces(tile):
            new_board = board.add(tile, coords, permutation)
            remaining_tiles_minus_this_one = remaining_tiles[:i] + remaining_tiles[i+1:]
            res = completed_board(new_board, remaining_tiles_minus_this_one)
            if res:
                return res
            # if this doesn't hit, try the next open space
    return None
    
tiles = [Tile(tilestr) for tilestr in open("inputs/day20").read().split("\n\n")]


final = solve_puzzle(tiles)

im = final.image_list()



# i have the image - let's rotate and flip it a few times
def count_dragons(strboard):
    # check for each to see if the mask fits
    # i'm sure there's a better way to do this but ...

    # wondering if i can just use a regex here ...
    line_length=str(SQUARE_LEN-20+1)
    mask = re.compile("#(..{"+line_length+"})#(....)##(....)##(....)###(.{"+line_length+"}.)#(..)#(..)#(..)#(..)#(..)#", \
                      re.MULTILINE | re.DOTALL)
    replace = r"O\1O\2OO\3OO\4OOO\5O\6O\7O\8O\9O\10O"

    processed, num_dragons = re.subn(mask, replace, strboard)
    with open("day20.output.image","w") as f:
        f.write(processed)
    
    roughness = processed.count("#")
    
    return num_dragons, roughness

   

for line in correct_orientation.split("\n"):
    for tile_id in line.strip().split(" "):
        



# just need to rotate and flip it several times
lines = [list(row) for row in im.split("\n")]
SQUARE_LEN=SQUARE_SIZE*8

for n_rotations in range(4):
    for to_flip in (False, True):

        print(f"rotate {n_rotations} times and flip {to_flip}")
        
        newlines = lines.copy()
        def r(i,j):
#            print("rotate",(i,j))
            return newlines[SQUARE_LEN-1-j][i]
        def f(i,j):
#            print(f"newlines {len(newlines)} {SQUARE_LEN} {len(newlines[0])}")
#            print("flip",(i,j)," and ",SQUARE_LEN-1-j)
            return newlines[i][SQUARE_LEN-1-j]

#        print("---\n   " + "\n   ".join(["".join(line) for line in newlines]))

        for n in range(n_rotations): # rotate this number
            newlines = [ [r(i,j) for j in range(SQUARE_LEN)] for i in range(SQUARE_LEN) ]
#            print(f"rotation {n}")
#            print("---\n   " + "\n   ".join(["".join(line) for line in newlines]))

        if to_flip:
#            print("flip")
            newlines = [ [f(i,j) for j in range(SQUARE_LEN)] for i in range(SQUARE_LEN) ]
#            print("---\n   " + "\n   ".join(["".join(line) for line in newlines]))

        strboard = "\n".join(["".join(line) for line in newlines])
        print(strboard)

        n_dragons, roughness = count_dragons(strboard)
        if n_dragons > 0:
            print("n dragons ", n_dragons)
            print("roughness", roughness)
            sys.exit()
            # todo: calculte the answer


dragon_sample = """.####...#####..#...###..
#####..#..#.#.####..#.#.
.#.#...#.###...#.##.##..
#.#.##.###.#.##.##.#####
..##.###.####..#.####.##
...#.#..##.##...#..#..##
#.##.#..#.#..#..##.#.#..
.###.##.....#...###.#...
#.####.#.#....##.#..#.#.
##...#..#....#..#...####
..#.##...###..#.#####..#
....#.##.#.#####....#...
..##.##.###.....#.##..#.
#...#...###..####....##.
.#.##...#.##.#.#.###...#
#.###.#..####...##..#...
#.###...#.##...#.######.
.###.###.#######..#####.
..##.#..#..#.#######.###
#.#..##.########..#..##.
#.#####..#.#...##..#....
#....##..#.#########..##
#...#.....#..##...###.##
#..###....##.#...##.##.#"""

#print(count_dragons(dragon_sample, dragon_mask))

# underperforming - not quite matching the dragon sample with my own stuff

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
