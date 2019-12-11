from intcode import IntCodeComputer

directions = [ (0,1), (1,0), (0,-1), (-1,0) ]

def panels(program, initial_input):
    cells = {}

    c = IntCodeComputer(program)
    current_cell = (0,0)
    direction = (0,1)
    
    cells[current_cell] = initial_input

    while True:
        print("looping once")
        # first, give the input of the current panel
        if current_cell in cells:
            input = cells[current_cell]
        else:
            input = 0

        c.add_input(input)

        o1 = c.compute()
        c.clear_output()
        if len(o1) == 0:
            return cells
        
        o2 = c.compute()
        c.clear_output()

        color = o1
        
        # paint the cell!
        cells[current_cell] = color
        print(f"{current_cell} is now {color}")

        turn_direction = o2
        direction = next_direction(direction, turn_direction)
        
        # then move!
        current_cell = ((current_cell[0] + direction[0]), (current_cell[1] + direction[1]))

def next_direction(current, turn_direction):
    
    current_direction_i = directions.index(current)
    turn_direction = int(turn_direction)
    if turn_direction == 0:
        turn_direction = -1

    return directions[(current_direction_i + turn_direction ) % len(directions)]

def printcells(cells):
    cells = [cell for cell, value in cells.items() if int(value) == 1]
    print(cells)

    xs = [cell[0] for cell in cells]
    ys = [cell[1] for cell in cells]

    width = max(xs) - min(xs)
    height = max(ys) - min(ys)

    x_offset = min(xs)
    y_offset = min(ys)

    out = ""
    for i in reversed(range(y_offset, height)):
        for j in range(x_offset, width):
            if (j,i) in cells:
                char = "#"
            else:
                char = " "
            print((i,j), char)
            out += char
        out += "\n"
    print(out)

program = "3,8,1005,8,319,1106,0,11,0,0,0,104,1,104,0,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,1001,8,0,28,2,1008,7,10,2,4,17,10,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,0,10,4,10,1002,8,1,59,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,1001,8,0,81,1006,0,24,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,102,1,8,105,2,6,13,10,1006,0,5,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,1002,8,1,134,2,1007,0,10,2,1102,20,10,2,1106,4,10,1,3,1,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,1002,8,1,172,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,101,0,8,194,1,103,7,10,1006,0,3,1,4,0,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,101,0,8,228,2,109,0,10,1,101,17,10,1006,0,79,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,1002,8,1,260,2,1008,16,10,1,1105,20,10,1,3,17,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,1002,8,1,295,1,1002,16,10,101,1,9,9,1007,9,1081,10,1005,10,15,99,109,641,104,0,104,1,21101,387365733012,0,1,21102,1,336,0,1105,1,440,21102,937263735552,1,1,21101,0,347,0,1106,0,440,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21102,3451034715,1,1,21101,0,394,0,1105,1,440,21102,3224595675,1,1,21101,0,405,0,1106,0,440,3,10,104,0,104,0,3,10,104,0,104,0,21101,0,838337454440,1,21102,428,1,0,1105,1,440,21101,0,825460798308,1,21101,439,0,0,1105,1,440,99,109,2,22101,0,-1,1,21102,1,40,2,21101,0,471,3,21101,461,0,0,1106,0,504,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,466,467,482,4,0,1001,466,1,466,108,4,466,10,1006,10,498,1102,1,0,466,109,-2,2105,1,0,0,109,4,2101,0,-1,503,1207,-3,0,10,1006,10,521,21101,0,0,-3,21202,-3,1,1,22102,1,-2,2,21101,1,0,3,21102,540,1,0,1105,1,545,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,568,2207,-4,-2,10,1006,10,568,22102,1,-4,-4,1106,0,636,22102,1,-4,1,21201,-3,-1,2,21202,-2,2,3,21102,587,1,0,1105,1,545,21201,1,0,-4,21101,0,1,-1,2207,-4,-2,10,1006,10,606,21102,0,1,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,628,22102,1,-1,1,21102,1,628,0,105,1,503,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2106,0,0"

#print(len(panels(program, 1)))

printcells(panels(program, 1))
