# An Intcode program is a list of integers separated by commas (like 1,0,0,3,99). To run one,
# start by looking at the first integer (called position 0). Here, you will find an
# opcode - either 1, 2, or 99. The opcode indicates what to do; for example, 99 means
# that the program is finished and should immediately halt. Encountering an unknown opcode means something went wrong.

# Opcode 1 adds together numbers read from two positions and stores the result in a third position. The three integers immediately after the opcode tell you these three positions - the first two indicate the positions from which you should read the input values, and the third indicates the position at which the output should be stored.

# For example, if your Intcode computer encounters 1,10,20,30, it should read the values at positions 10 and 20, add those values, and then overwrite the value at position 30 with their sum.


# Once you're done processing an opcode, move to the next one by stepping forward 4 positions.


def compute(input, noun=None, verb=None):

    inputs = [int(i) for i in input.split(",")]

    if noun:
        inputs[1] = noun
    if verb:
        inputs[2] = verb

    for i in range(0, len(inputs), 4):
        # dummy op for example code
        opcode = inputs[i]

        # Opcode 1 adds together numbers read from two positions and stores
        # the result in a third position. The three integers immediately
        # after the opcode tell you these three positions - the first two
        # indicate the positions from which you should read the input values,
        # and the third indicates the position at which the output should be stored.
        if opcode == 1:
            output = inputs[inputs[i+1]] + inputs[inputs[i+2]]
            inputs[inputs[i+3]] = output
            
        # Opcode 2 works exactly like opcode 1, except it multiplies the two inputs
        # instead of adding them. Again, the three integers after the opcode indicate
        # where the inputs and outputs are, not their values.
        elif opcode == 2:
            output = inputs[inputs[i+1]] * inputs[inputs[i+2]]
            inputs[inputs[i+3]] = output
            
        # 99 means that the program is finished and should immediately halt.
        elif opcode == 99:
            return ",".join([str(i) for i in inputs])

        else:
            assert("This is not a corect opcode" + str(opcode) + " at position " + str(i))
    
# provided unit tests
assert(compute("1,0,0,0,99") == "2,0,0,0,99")
assert(compute("2,3,0,3,99") == "2,3,0,6,99")
assert(compute("2,4,4,5,99,0") == "2,4,4,5,99,9801")
assert(compute("1,1,1,4,99,5,6,0,99") == "30,1,1,4,2,5,6,0,99")

# my provided input
input = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,5,19,23,2,9,23,27,1,6,27,31,1,31,9,35,2,35,10,39,1,5,39,43,2,43,9,47,1,5,47,51,1,51,5,55,1,55,9,59,2,59,13,63,1,63,9,67,1,9,67,71,2,71,10,75,1,75,6,79,2,10,79,83,1,5,83,87,2,87,10,91,1,91,5,95,1,6,95,99,2,99,13,103,1,103,6,107,1,107,5,111,2,6,111,115,1,115,13,119,1,119,2,123,1,5,123,0,99,2,0,14,0"

# Part 1:
# before running the program, replace position 1 with the value 12 and replace position 2 with the value 2. What value is left at position 0 after the program halts?
# We put these into parameters
print("Part 1:")
print(compute(input, 12, 2))

# Part 2: what is the input that causes the program to produce the output 19690720?
# let's see what the shape is ... then after running look at what produces that output
for i in range(100):
    for j in range(101):
        r = compute(input,i,j).split(",")[0]
        if int(r) == 19690720:
            print(f"compute({i},{j}) = {r}")
            print(f"Part 2: {i * 100 + j}")
