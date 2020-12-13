import math
import fileinput

lines = list(fileinput.input())

earliest = int(lines[0])
bus_strs = lines[1]


def earliest_dept(earliest, bus_strs):
    buses = [int(num) for num in bus_strs.split(",") if num != 'x']
    
    next_times = dict()
    print(buses)
    for bus in buses:
        rem = earliest % bus
        if rem == 0:
            return bus
        else:
            next_times[bus] = bus - rem

    m = min(next_times, key=next_times.get)
    return m * next_times[m]

def earliest_sequential(bus_strs):
    buses = dict((int(num), i) for i, num in enumerate(bus_strs.split(",")) if num != 'x')

    print(buses)

    # going to accelerate, looking first for the next biggest
    num = 1
    increment = 1
    
    print(buses.items())
    for bus, offset in sorted(buses.items(), reverse=True):
        print("bus",bus,"offset",offset,"num",num,"increment", increment)
        while((num + offset) % bus != 0):
            bus_checks = [ (b, (num + offset) % b) for b, offset in buses.items()]
            print(num, bus_checks)
            num += increment

        # found one that satisfies this
        increment = increment * bus

    return num

    print(bus, offset)
    
    num_digits = 0
    while True:
        i += max_bus
        if num_digits < int(math.log(i,10)):
            num_digits = int(math.log(i,10))
            print(str(i) + " has " + str(num_digits+1) + " digits")
        # check against all the others
        bus_checks = [ (i + offset) % bus == 0 for bus, offset in buses.items()]
        #if (i>1068000): # 1068781
        #    print(i, bus_checks)
        if all(bus_checks):
            return i

        

print(earliest_sequential(bus_strs))
