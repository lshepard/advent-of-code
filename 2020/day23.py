inp = """284573961"""
from tqdm import tqdm

def create_list(cups_string, max_len=None):
   nums = [int(i) for i in list(cups_string)]
   if max_len:
       nums += list(range(max(nums)+1, max_len+1))
   nodes = dict()

   first = nums[0]
   prev = None
   for i in nums:
       if prev:
           nodes[prev] = i
       prev = i

   # finally, link the last one to the first one so it's a cycle
   nodes[prev] = first

   return nodes

def nodes_str(nodes, start_index):
    n = start_index
    s = str(n)
    for i in range(1,len(nodes)):
        n = nodes[n]
        s += "," + str(n)
    return s
        
def moves(nodes, max_length, num_moves, start):

    current = start
    for x in tqdm(range(num_moves)):
        #print(nodes)
        #print(nodes_str(nodes, current))
        
        # The crab picks up the three cups that are immediately clockwise of the current cup.
        p1 = nodes[current]
        p2 = nodes[p1]
        p3 = nodes[p2]
        picked = set([p1, p2, p3])

        #print("picked", [p1,p2,p3])
        # They are removed from the circle; cup spacing is adjusted as necessary to maintain the circle.
        nodes[current] = nodes[p3]
        nodes[p3] = None
        #print(nodes)
        
        # The crab selects a destination cup: the cup with a label equal to the current cup's label minus one.
        di = None
        for i in range(1, max_length):
            di = (current - i - 1) % max_length + 1
            #print("---testing " + str(di))
            if di not in picked:
                #print(" -- cant choose " + str(di) + " its in picked")
                break
        #print("chose " + str(di))    
            
        # The crab places the cups it just picked up so that they are immediately clockwise
        # of the destination cup. They keep the same order as when they were picked up.
        #print("destination", di)
        #print("setting p3 ", p3 , "to ", nodes[di])
        nodes[p3] = nodes[di]
        nodes[di] = p1
        #print("before choosing" , nodes, "current still ", current, "next current", nodes[current])    
        # The crab selects a new current cup: the cup which is immediately clockwise of the current cup.
        current = nodes[current]
            
    return (nodes, current)

if False:
    part1_nodes = create_list("389125467")
    (nodes, current_index) = moves(part1_nodes, len(part1_nodes), 10, start=3)
    
    # After the crab is done, what order will the cups be in?
    # Starting after the cup labeled 1, collect the other cups' labels clockwise
    # into a single string with no extra characters; each number except 1 should
    # appear exactly once.
    s = nodes_str(nodes, 1)
    print("Part 1", s[:-1])


# now on to part 2

#part2_nodes = create_list("389125467", 1_000_000)
part2_nodes = create_list(inp, 1_000_000)
print(nodes_str(part2_nodes,2))
(nodes, current_index) = moves(part2_nodes, len(part2_nodes), 10_000_000, start=2)
p1 = nodes[1]
p2 = nodes[p1]
print(p1, p2)
print(p1 * p2)
