import cProfile

import re
import sys
import tqdm

"""
This solves part 1 of the challenge. Turns out for part 2, that it's basically impossible
to calculate for 50 billion iterations, regardless of the algorithm efficiency. I played
with matrix multiplication etc. But eventually I just printed out the scores,
plugged it into Excel and realized that after a while, each generation just added 42 to
the score. So I multiplied it out and got the answer!
"""


def process(inpt, num_gens, display=False):
    """Runs through - displays the state if asked, otherwise just output the running score"""
    # first line is initial state
    r = re.compile("([.#]{5}) => ([.#])")
    
    state = inpt[0][15:].rstrip("\n")
    first_n = 0
    rules = dict(tuple(r.match(row).groups()) for row in inpt[2:])
    gen = 0
    print(rules)

    print(gen,first_n,state)

    states = [(first_n, state, gen)]
    min_n = -20
    s = None
    
    for i in tqdm.tqdm(range(num_gens)):
        state, first_n = generation(state, first_n, rules)
        gen += 1
        min_n = min(min_n, first_n)
        s = score(state, first_n)
        if display:
            print (s, ('.' * (first_n - min_n)) + state)
        else:
            print(s)

    return s 
    
def generation(state, first_n, rules):
    """Return the next state. First_n is what the number of the first char in the string is."""

    state = "...." + state + "...."
    first_n -= 2 # adding 4 dots, but only add 2 to the first_n because we start at 2 below

    new_state = "".join([rules.get(state[i:i+5],".") for i in range(len(state))])

    first_pot = new_state.find("#")
    first_n += first_pot

    last_pot = new_state.rfind("#")
    
#    print(f"first pot {first_pot} in {new_state}")
    return new_state[first_pot:last_pot+1], first_n

def score(state, first_n):
    """Calculate sum of the numbers of all the pots which contain a plant"""

    return sum([(i + first_n) for i, letter in enumerate(state) if letter == "#"])
    

if __name__ == "__main__":
    inpt = sys.stdin.readlines()
    
    print(process(inpt,10000,False))

