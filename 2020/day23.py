inp = """284573961"""

def next_move(cups):
    """Perform actions for each move, given a list of cups."""

    current = cups[0]
    
    # The crab picks up the three cups that are immediately clockwise of the current cup.
    # They are removed from the circle; cup spacing is adjusted as necessary to maintain the circle.
    picked_up = cups[1:4]
    remaining = [ cups[0] ] + cups[4:]

    # The crab selects a destination cup: the cup with a label equal to the current cup's label minus one.
    destination_i = None
    i = 1
    while True:
        # If at any point in this process the value goes below the lowest value on any cup's label,
        # it wraps around to the highest value on any cup's label instead.

        try:
            # If this would select one of the cups that was just picked up, the crab will keep subtracting one
            # until it finds a cup that wasn't just picked up.
            destination_i = remaining.index((current - i-1) % len(cups) + 1)
            break
        except:
            i += 1
            next

    print("destination: " + str(remaining[destination_i]))
    
    # The crab places the cups it just picked up so that they are immediately clockwise
    # of the destination cup. They keep the same order as when they were picked up.
    # The crab selects a new current cup: the cup which is immediately clockwise of the current cup.

    # new order: the three picked up, then the remaining items up to current cup, then the rest up to the destination cup
    return remaining[1:destination_i+1] + picked_up + remaining[destination_i+1:] + [ remaining[0] ]


cups = [int(i) for i in list("389125467")]
cups = [int(i) for i in list(inp)]
for i in range(100):
    print(cups)
    cups = next_move(cups)

# After the crab is done, what order will the cups be in?
# Starting after the cup labeled 1, collect the other cups' labels clockwise
# into a single string with no extra characters; each number except 1 should
# appear exactly once.

one_index = cups.index(1)
print("".join([str(c) for c in  cups[one_index+1:] + cups[:one_index]]))
