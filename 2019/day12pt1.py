import re
import itertools
import numpy as np

inpt = open("day12.input").read()

class Moon():
    def __init__(self, x, y, z, vx, vy, vz):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz
        
    def apply_gravity(self, other_moons):
        for other_moon in other_moons:
            self.apply_one_gravity(other_moon)

    def apply_one_gravity(self, other_moon):
        """Note that it happens to work to noop if given self"""
        self.vx += np.sign(other_moon.x - self.x)
        self.vy += np.sign(other_moon.y - self.y)
        self.vz += np.sign(other_moon.z - self.z)

    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz
#        self.step = self.step + 1
        
    def energy(self):
        return self.potential() * self.kinetic()

    def potential(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def kinetic(self):
        return abs(self.vx) + abs(self.vy) + abs(self.vz)

    def __repr__(self):
#        return f"pos:({self.x},{self.y},{self.z}) \tvel:({self.vx},{self.vy},{self.vz}) \tpot:{self.potential()} kin:{self.kinetic()} tot:{self.energy()}"
        return f"pos:({self.x},{self.y},{self.z}) \tvel:({self.vx},{self.vy},{self.vz})"

def in_scans(inpt):
    p = re.compile("<x=([-0-9]+), y=([-0-9]+), z=([-0-9]+)>")
    axes = []
    for row in inpt.split("\n"):
        x, y, z = re.match(p, row).groups()
        axes.append( Moon(int(x),int(y),int(z),0,0,0))
    return axes

def step(moons):

    for m in moons:
        m.apply_gravity(moons)

    for m in moons:
        m.step()
    
def day12(inpt):


    return ""
    

sample = """<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>"""

#assert(in_scans(sample) == [ (-1,0,2,0,0,0), (2,-10,-7,0,0,0), (4,-8,8,0,0,0), (3,5,-1,0,0,0) ])

input = """<x=-3, y=10, z=-1>
<x=-12, y=-10, z=-5>
<x=-9, y=0, z=10>
<x=7, y=-5, z=-3>"""

def day12pt2():
    moons = in_scans(input)
    positions = set()
    while True:
        rep = "\t".join([str(moon) for moon in moons])
        if rep in positions:
            print(i)
            positions.add(rep)
        print(f"{rep}")
        step(moons)

# part 1
#print(sum([moon.energy() for moon in moons]))



day12pt2()
