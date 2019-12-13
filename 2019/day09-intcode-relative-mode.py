from intcode import IntCodeComputer

p1 = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
c = IntCodeComputer("109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99", 0)
c.compute()
o = c.output()
print(o)
assert(o == p1)


def part1(program):
    c = IntCodeComputer(program, 1)
    c.add_input(1)
    c.compute()
    return c.output()


def part2(program):
    c = IntCodeComputer(program, 2)
    c.add_input(2)
    c.compute()
    return c.output()

inpt = open("day9.input").read()
#print(part1(inpt))
print(part2(inpt))
