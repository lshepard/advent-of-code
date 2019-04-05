import sys
import re

def process_polymer(inpt):
    """take an array of characters"""
    chars = list(inpt)
    try_again = True
#    print("".join(chars))

    
    while try_again:
        # look at each 2-ple, can it be destroyed?
#        print("outer loop", inpt)
        try_again = False
        
        for i in range(len(chars)-1):
            l = chars[i]
            r = chars[i+1]
            
            if (l.lower() == r.lower() and (l != r)):
                del chars[i+1]
                del chars[i]
                try_again = True
#                print("match!", len(chars), l, r, "index", i)
#                print("".join(chars))
                break
                
    return len(chars)
    
def shortest_with_remove(inpt):
    """Remove all instances of a given polymer"""
    mins = []
    for unit in {i.lower() for i in inpt}:
        r = re.compile(unit, re.IGNORECASE)
        without_unit = r.sub("",inpt)
        l = process_polymer(without_unit)
        print("without ", unit, " length ", len(without_unit), " min ", l)
        mins.append(l)

    return min(mins)



if __name__ == "__main__":
    text = sys.stdin.read()
    print(shortest_with_remove(text))

    
