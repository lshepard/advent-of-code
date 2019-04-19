from tqdm import tqdm

import sys
pbar = None

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

def window_powers_max(serial, window):
    """Return max for a window of size 3 (part 1)"""
    powers = dict()
    window_powers(0,0, serial, 300, powers)
    
    three_powers = dict(((x,y,w),v) for (x,y,w), v in powers if w == 3)
    
    m = max(three_powers, key=three_powers.get)
    return tuple(m[0:1])


# We'll use dynamic programming

# Start by looking at the answer, then recurse for each smaller cell

# If we are looking only at a single cell, return the value provided

# add value to a dict as we go

def window_powers(x, y, serial, window, previous):
    # if this is already calculated, then return it
    key = (x,y,window)

    if key not in previous:
        if pbar:
            pbar.update(len(previous))

        if len(previous) % 10000 < 10:
            print("calculating",x,y,window,"previouslen",len(previous))
        if window == 1:
            previous[key] = cell(x,y,serial)
        else:
            # lets find the max's of all possibly sub-squares

            # there are four


            # otherwise, it's composed of the smaller ones

            [ (x,      y),
              (x + 1 , y),
              (x,      y + 1),
              (x + 1,  y + 1) ]


            topleft = window_powers(x, y, serial, window-1, previous) + \
                      sum([window_powers(i, y+window-1, serial, 1, previous) for i in range(x, window)]) + \
                      sum([window_powers(x+window-1, j, serial, 1, previous) for j in range(y, window - 1)])

            topright = window_powers(x + 1, y, serial, window-1, previous) + \
                      sum([window_powers(i, y+window-1, serial, 1, previous) for i in range(x, window)]) + \
                      sum([window_powers(x,          j, serial, 1, previous) for j in range(y, window - 1)])
            
            botleft = window_powers(x, y + 1, serial, window-1, previous) + \
                      sum([window_powers(i,          y, serial, 1, previous) for i in range(x, window)]) + \
                      sum([window_powers(x+window-1, j, serial, 1, previous) for j in range(y+1, window)])

            botright = window_powers(x + 1, y + 1, serial, window-1, previous) + \
                      sum([window_powers(i,          y, serial, 1, previous) for i in range(x, window)]) + \
                      sum([window_powers(x,          j, serial, 1, previous) for j in range(y+1, window)])

            previous[key] = max([topleft, topright, botleft, botright])
    
    return previous[key]

def window_powers_max_any(width, height, serial):

    previous = dict()
    
    powers = dict(((i,j,w),window_powers(i,j,serial,w,previous))
                  for w in tqdm.tqdm(range(1,300))
                  for i in range(1,300)
                  for j in range(1,300))
        
    return max(previous, key=previous.get)

if __name__ == "__main__":

    pbar = tqdm(total=300**3)
    p = dict()
    print(window_powers_max(18,3))
    pbar.close()
#    print(p)
#    print(window_powers(300,300,7857,3))
#    print(window_powers_max_any(300,300,7857))

assert(cell(3,5,8) == 4)
assert(cell(122,79,57) == -5)
assert(cell(217,196,39) == 0)

assert(window_powers_max(300,300,18) == (33,45))
assert(window_powers_max(300,300,42) == (21,61))

assert(window_powers_max_any(300,300,18) == (90,269,16))
