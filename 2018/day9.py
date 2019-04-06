import cProfile

import re
import sys
import tqdm
#from blist import blist
import numpy as np

def marbles(num_players, num_marbles, display=False):

    board = [0]
    current = 0
    scores = dict((i,0) for i in range(num_players)) # everyone starts at 0
    current_player = 0
    current_length = 1
    
    for i in tqdm.tqdm(range(1, num_marbles+1)):
        if display:
            print(" ".join(["*"+str(s)+"*" if i==current else str(s)
                            for i, s in enumerate(board)]))
        
        if i % 23 == 0:
            # if the marble that is about to be placed has a number which
            # is a multiple of 23, something entirely different happens.
            
            # - the current player keeps the marble they would have placed,
            # adding it to their score.
            scores[current_player] += i
            
            # - the marble 7 marbles counter-clockwise from the current marble
            # is removed from the circle and also added to the current player's score.
            to_remove = (current-7) % current_length
            scores[current_player] += board.pop(to_remove)
            current_length -= 1
            
            # - The marble located immediately clockwise of the marble that
            # was removed becomes the new current marble.
            current = to_remove

        else:
            # each Elf takes a turn placing the lowest-numbered remaining
            # marble into the circle between the marbles that are 1 and 2
            # marbles clockwise of the current marble
            current = (current+2) % current_length
            board.insert(current, i)
            current_length += 1

        current_player = (current_player + 1) % num_players

    return max(scores.values())

print(marbles(9, 25, display=True))
cProfile.run("marbles(473, 709040, display=False)")
