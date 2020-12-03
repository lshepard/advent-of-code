def read_input(inp):
    return [list(row) for row in inp]

def count_trees(inp, num_right, num_down):
    lines = read_input(inp)
    line_length = len(inp[0].strip())
    
    i = 0
    j = 0

    trees = 0
    #print("length",line_length)
    while j < len(lines):
        c = lines[j][i]
        if c == "#":
            trees += 1
        #print(i,j,c,trees)
        
        i = (i + num_right) % line_length
        j += num_down
        

    return trees
    

test = open('inputs/day03.test').readlines()
print("test",count_trees(test,3,1))

real = open('inputs/day03').readlines()
print("part1",count_trees(real,3,1))

a = count_trees(real, 1, 1)
b = count_trees(real, 3, 1)
c = count_trees(real, 5, 1)
d = count_trees(real, 7, 1)
e = count_trees(real, 1, 2)
print("part2", a*b*c*d*e)
