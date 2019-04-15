import tqdm

import sys

def cell(x, y, serial):
    return ((x+10) * (y * (x+10) + serial) // 100) % 10 - 5

def cell_powers(width, height, serial):
    coords = [(i,j) for j in range(height) for i in range(width)]
    return dict(((i,j), cell(i,j,serial)) for (i,j) in coords)

def window_powers(width, height, serial, window):
    
    cp = cell_powers(width, height, serial)
    
    return dict(((i,j),
                 sum([cp[(x,y)]
                      for x in range(i,i+window)
                      for y in range(j,j+window)]))
                 for j in range(height-window)
                 for i in range(width-window))

def window_powers_max(width, height, serial, window=3):
    """Return max for a window of size 3 (part 1)"""
    powers = window_powers(width, height, serial, window)
    return max(powers, key=powers.get)

def all_window_powers(width, height, serial):
    return dict(((x,y,w), value)
                for w in tqdm.tqdm(range(1,300))
                for (x,y),value in window_powers(width, height, serial, w).items())

def window_powers_max_any(width, height, serial):
    """Find the max of ANY window size (part 2)"""
    powers = all_window_powers(width, height, serial)
    return max(powers, key=powers.get)

if __name__ == "__main__":
    pass
#    print(window_powers(300,300,7857,3))
#    print(window_powers_max_any(300,300,7857))

assert(cell(3,5,8) == 4)
assert(cell(122,79,57) == -5)
assert(cell(217,196,39) == 0)

assert(window_powers_max(300,300,18) == (33,45))
assert(window_powers_max(300,300,42) == (21,61))

assert(window_powers_max_any(300,300,18) == (90,269,16))
