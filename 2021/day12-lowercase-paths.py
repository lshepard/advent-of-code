from collections import defaultdict
from collections import Counter

import math
import fileinput

test = """start-A
start-b
A-c
A-b
b-d
A-end
b-end""".split("\n")

big_test = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW""".split("\n")

real_input = """we-NX
ys-px
ys-we
px-end
yq-NX
px-NX
yq-px
qk-yq
pr-NX
wq-EY
pr-oe
wq-pr
ys-end
start-we
ys-start
oe-DW
EY-oe
end-oe
pr-yq
pr-we
wq-start
oe-NX
yq-EY
ys-wq
ys-pr""".split("\n")

def parse_graph(lines):
    g = dict()
    for line in lines:
        left, right = line.split("-")
        g[left] = g.get(left, set())
        g[left].add(right)

        g[right] = g.get(right, set())
        g[right].add(left)
    return g

def dfs(graph, node, path_so_far=[]):
    """Depth first traversal, short-circuit if visit lowercase node twice"""
    #print(f"dfs {node} path so far {path_so_far}")

    if node == "end":
        return [ path_so_far  + ["end"] ]
    if node == "start" and node in path_so_far:
        # cant visit start again
        return []
    elif ((node.lower() == node) and
          (node in path_so_far) and
          # check if any other small node has been visited more than once
          max([v for k, v in Counter(path_so_far).items() if k.lower() == k]) > 1):
        # lowercase cant be visited --twice--
        #print(f"skipping lowercase {node} that appears too many ")
        return []
    else:
        next_nodes = graph.get(node,set())
        paths = []
        for next_node in next_nodes:
            paths = paths + dfs(graph, next_node, path_so_far + [node])
        return paths
    
def part1(inp):
    g = parse_graph(inp)
    print(g)
    paths = dfs(g, "start")
    return paths

paths = part1(test)
print(len(paths))
for path in paths:
    print(",".join(path))
#print(len(part1(big_test)))
print(len(part1(real_input)))
    
