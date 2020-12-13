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
    buses = [int(num) for num in bus_strs.split(",")]


    equation is :

    ni =
    
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


print(earliest_dept(earliest, bus_strs))
