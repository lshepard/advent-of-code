import cProfile

import re
import sys
import tqdm

def lastten(num_recipes):
    """part 1"""
    current_elf = [0,1]
    scores = [3, 7]
    num_scores = len(scores)

    while True:
        # add the new ones to the end
        new_score = sum([scores[elf] for elf in current_elf])
        
        new_list = [int(c) for c in list(str(new_score))] # add each digit to the end
        num_scores += len(new_list)
        scores.extend(new_list)
        
        # step for each elf
        current_elf = [(elf + scores[elf] + 1) % num_scores for elf in current_elf]

        if num_scores >= num_recipes + 10:
            break

    r =  "".join([str(s) for s in scores[num_recipes:num_recipes+10]])
    return r

def fiveleft(search_term):
    """part 2 - copy/pasted and modified"""
    current_elf = [0,1]
    scores = "37"
    num_scores = len(scores)

    while True:
        # add the new ones to the end
        new_score = str(sum([int(scores[elf]) for elf in current_elf]))
        num_scores += len(new_score)
        last_few = scores[-8:]
        scores += new_score
        
        # step for each elf
        current_elf = [(elf + int(scores[elf]) + 1) % num_scores for elf in current_elf]
        if num_scores % 1000000 == 0:
            # give me a sense of progress as it chugs
            print(num_scores)

        # i'm checking just the last few characters - reason to avoid an n^2
        # situation. no need to check all previous characters every time,
        # only those that were just added
        if ((last_few + new_score).find(search_term) > -1):
            return scores.find(search_term)
        
if __name__ == "__main__":

    assert(lastten(9) == "5158916779")
    assert(lastten(5) == "0124515891")
    assert(lastten(18) == "9251071085")
    assert(lastten(2018) == "5941429882")

    assert(fiveleft("51589") == 9)
    assert(fiveleft("01245") == 5)
    assert(fiveleft("92510") == 18)
    assert(fiveleft("59414") == 2018)
    
    print(fiveleft("236021"))
