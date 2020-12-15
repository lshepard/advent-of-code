import copy
from collections import Counter

test = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""



def part1(lines):

    board = [list(line) for line in lines]
    print("len",len(board))
    print(board_str(board))
    move_num = 0
    
    while True:
        newboard = [list(line) for line in board]
        
        
        for i, row in enumerate(inp):
            for j, cell in enumerate(row):
                newboard[i][j] = nextmove(board, i, j)
        if board_str(newboard) == board_str(board):
            return Counter(list(board_str(board)))
        move_num += 1
        print("Move " + str(move_num))
        print( board_str(board))
        board = copy.deepcopy(newboard)
    

def part2(lines):
    """Ray tracing occupancy by visibility"""
    
    board = [list(line) for line in lines]
    move_num = 0
    
    while True:
        newboard = [list(line) for line in board]
        
        for i, row in enumerate(inp):
            for j, cell in enumerate(row):
                newboard[i][j] = nextmove2(board, i, j)
        if board_str(newboard) == board_str(board):
            return Counter(list(board_str(board)))
        move_num += 1
#        print("Move " + str(move_num))
#        print( board_str(board))
        board = copy.deepcopy(newboard)
    
def board_str(board):
    return "\n".join(["".join(row) for row in board])
    
def getcell(board, i, j):
    
    if i >= 0 and i < len(board) and j >= 0 and j < len(board[0]):
        return board[i][j]
    else:
        return ";"
    
def nextmove(board, i, j):
    relatives = [(-1,-1), (-1,0), (-1,1),
                 (0, -1),         (0, 1),
                 (1, -1), (1, 0), (1, 1)]
    adj_cells = [getcell(board, i+x, j+y) for (x,y) in relatives]
    this_cell = getcell(board, i, j)

    counts = Counter(adj_cells)
#    print(i, j, this_cell, counts, adj_cells)
    if this_cell == "L" and counts.get("#",0) == 0:
        return "#"
    elif this_cell == "#" and counts.get("#",0) >= 4:
        return "L"
    else:
        return this_cell


def get_visible_cell(board, i, j, di, dj):
    """find the next visible cell from i,j in the di,dj direction"""
    c = getcell(board, i+di, j+dj)
#    print(c,i,j,di,dj)
    if c == ".":
        return get_visible_cell(board, i+di, j+dj, di, dj)
    else:
        return c
    
def nextmove2(board, i, j):
    """Also, people seem to be more tolerant than you expected: it now takes five or more visible occupied seats for an occupied seat to become empty (rather than four or more from the previous rules). The other rules still apply: empty seats that see no occupied seats become occupied, seats matching no rule don't change, and floor never changes.
"""
    relatives = [(-1,-1), (-1,0), (-1,1),
                 (0, -1),         (0, 1),
                 (1, -1), (1, 0), (1, 1)]

    adj_cells = [get_visible_cell(board, i, j, x, y) for (x,y) in relatives]
    this_cell = getcell(board, i, j)

    counts = Counter(adj_cells)
#    print(i, j, this_cell, counts, adj_cells)
    if this_cell == "L" and counts.get("#",0) == 0:
        return "#"
    elif this_cell == "#" and counts.get("#",0) >= 5:
      #  print("switching to # ",i,j,counts)
        return "L"
    else:
        return this_cell


    
inp = open("inputs/day11").readlines()
#inp = test.split("\n")
#print("Part 1")
#print(part1(inp))

print("Part 2")
print(part2(inp))
