import re
import fileinput

lines ="""0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""".split("\n")
lines = list(fileinput.input())

def main(lines):

    cells = {}
    for line in lines:
        print(line)
        l,r = line.strip().split(" -> ")
        x1,y1 = l.split(",")
        x2,y2 = r.split(",")

        if x1 == x2:
            if int(y2) < int(y1):
                y1, y2 = y2, y1
            line = ( (x1, y1) , (x2 , y2))
                
#            print("samesies " + x1)
            for j in range(int(y1),int(y2)+1):
                cell = (int(x1), j)
                print(cell)
                cells[cell] = cells.get(cell, set())
                cells[cell].add(line)

        if y1 == y2:
            if int(x2) < int(x1):
                x1, x2 = x2, x1
            line = ( (x1, y1) , (x2 , y2))

            for i in range(int(x1),int(x2)+1):
                cell = (i, int(y1))
         #       print(cell)
                cells[cell] = cells.get(cell, set())
                cells[cell].add(line)


    # create a list of cells for each line
    # make a dic
#    print(cells)
    c = 0
    for cell in cells:
        if len(cells[cell]) >= 2:
            print(cell)
            c += 1
    return c

print(main(lines))

