
def count_orbits(orbits):

    all = {}
    for orbit in orbits:

        a, b = orbit.split(")")
        if a not in all:
            all[a] = []
        all[a].append(b)

    def count_orbit(item):
        # direct orbits
        if item in all:
            return len(all[item]) + sum([count_orbit(i) for i in all[item]])
        else:
            return 0
        
    return sum([count_orbit(key) for key in all.keys()])

def count_orbital_transfers(orbits):

    all = {}
    for orbit in orbits:

        a, b = orbit.split(")")
        if a not in all:
            all[a] = []
        if b not in all:
            all[b] = []
        #make it bidirectional
        all[a].append(b)
        all[b].append(a)

    print(all)
    
    def shortest_path(source, target, path):
        if source == target:
            return path

        """ How many moves to get to the target?"""
        other_nodes = [p for p in all[source] if p not in path]
        paths = [shortest_path(node, target, path + [source]) for node in other_nodes]
        paths = [p for p in paths if p is not None]
        print(f"{paths}")
        if len(paths) > 0:
            return min(paths, key=len)
        else:
            return None
        
    return len(shortest_path("YOU", "SAN", [])) - 2



test1 = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L""".split("\n")

assert(count_orbits(test1) == 42)


test2 = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN""".split("\n")

x = count_orbital_transfers(test2)
print(f"x = {x}")
assert(x == 4)

orbits = open("day6.input").read().split("\n")
print(count_orbital_transfers(orbits))
