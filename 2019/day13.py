from intcode import IntCodeComputer
import getch
import time
import numpy as np

def tiles(inpt):

    computer = IntCodeComputer(inpt)
    c = computer
    c.set_input_callback(input_callback)
    
    # insert quarters
    c.write_mem(0, 2)
    
    tiles = []
    ballx = 0
    while c:
        n = c.compute()
        o = computer.outputs
        tiles = [o[i:i+3] for i in range(0, len(o), 3)]
        print(f"Score: {scores(tiles)[-1]}")
        if len(o) == 0:
            break

prev_ballx = 20

def input_callback(outputs):
    global prev_ballx
    tiles = [outputs[i:i+3] for i in range(0, len(outputs), 3)]
    print(display(tiles))
#    print(f"Score: {scores(tiles)[-1]}")

    ballx = [t[0] for t in tiles if t[2] == 4][-1]
    ballvel = ballx - prev_ballx
    ballproj = ballx + ballvel
    
    paddlex = [t[0] for t in tiles if t[2] == 3][-1]
    prev_ballx = ballx

    
#    print(f"ballx {ballx} prev {prev_ballx} vel {ballvel} paddle {paddlex}")
#    time.sleep(.1)
    
    return np.sign(ballx - paddlex)

    char = getch.getch()
    print(char)
    if char == "j":
        return -1
    elif char == "l":
        return 1
    else:
        return 0        

def pt1(tiles):    
    return len([t for t in tiles if t[2] == 2])


def scores(tiles):
    return [t[2] for t in tiles if t[0] == -1 and t[1] == 0]

def display(tiles):

    xs = [t[0] for t in tiles]
    ys = [t[1] for t in tiles]

    tile_hash = {}
    for t in tiles:
        tile_hash[ (t[0],t[1]) ] = t[2]

    d = ""
    for i in range(max(ys)):
        for j in range(max(xs)):
            cell = (j,i)
            if cell in tile_hash:
                d += display_cell(tile_hash[cell])
            else:
                d += " "
        d += "\n"
    return d

def display_cell(val):
    """0 is an empty tile. No game object appears in this tile.
1 is a wall tile. Walls are indestructible barriers.
2 is a block tile. Blocks can be broken by the ball.
3 is a horizontal paddle tile. The paddle is indestructible.
4 is a ball tile. The ball moves diagonally and bounces off objects."""
    if val == 0:
        return " "
    elif val == 1:
        return "#"
    elif val == 2:
        return "O"
    elif val == 3:
        return "-"
    elif val == 4:
        return "o"
    else:
        return "X"

inpt = open("day13.input").read()
tiles = tiles(inpt)
print(display(tiles))
