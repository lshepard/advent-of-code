test = """F10
N3
F7
R90
F11"""

inp = open("inputs/day12").readlines()
#inp = test.split("\n")

def process(lines):
    
    x = 0
    y = 0
    d = 0 # index of directions

    directions = [ (1,0), (0,-1), (-1,0), (0,1) ]
    
    for line in lines:
        print(x,y,directions[d])
        print(line)
        direction = line[0]
        val = int(line[1:])

        if direction == "F":
            x += val * directions[d][0]
            y += val * directions[d][1]

        elif direction == "R":
            d = int(d + (val / 90)) % 4
        elif direction == "L":
            d = int(d - (val / 90)) % 4
        elif direction == "N":
            y = y+val
        elif direction == "S":
            y = y-val
        elif direction == "E":
            x = x+val
        elif direction == "W":
            x = x-val
        else:
            raise ValueError("invalid line " + line)

    print(x,y,directions[d])
    return abs(x) + abs(y)

                            
            
    

print(process(inp))
            
