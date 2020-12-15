import fileinput

inp = "1,2,16,19,18,0"

def how_many(inp, num):

    mem = dict()
    for i in range(1,num+1):

        # first speak the number
        if i <= len(inp):
            last = int(inp[i-1])
        else:
            
            
            if val is None: # last number was seen thefirst time
                last = 0
            else:
                last = i - val - 1
        
        val = mem.get(last,None)
        
        mem[last] = i
#        print(last, val, mem)
    return last

#print(how_many("0,3,6".split(","),2020))
#print(how_many(inp.split(","), 2020))
print(how_many(inp.split(","), 30000000))
