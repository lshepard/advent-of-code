import fileinput

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
        return b
        
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
                    self.open_spaces[rel_c][direction + 2 % 4] = flip(this_tile['permutation'][direction])
        #print("calculated " + str(len(self.open_spaces)) + " spaces")
        #print(self.open_spaces)

    def find_spaces(self, tile):
        """Finds all spaces that will work - returns the space and permutation of the tile that would fit there"""

        open_spaces_for_this_tile = [] # will be a list of tuples, each one containing the coords and permutation
        #print(self.open_spaces)
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
        bottom_edge = self.edgenum(lines[-1].strip())
        left_edge =   self.edgenum("".join([line[0] for line in lines[1:] ]))
        right_edge =  self.edgenum("".join([line[-1] for line in lines[1:] ]))

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
                              edges[1],
                              flip(edges[0]),
                              edges[3] ]
                permutations.append(edges)
        return permutations
        
        
    def __repr__(self):
        return "Tile " + str(self.id) + ": " + str(self.edges)

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
        "permutation": first_tile.permutations()[0]}})
    return completed_board(board,remaining_tiles)

def completed_board(board, remaining_tiles):
    """Recursive function to calculate a given board state"""

    print("board", board)
    
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
    
tiles = [Tile(tilestr) for tilestr in open("inputs/day20.sample").read().split("\n\n")]

for tile in tiles:
    print ("Tile", tile.id, tile.permutations())

solve_puzzle(tiles)
