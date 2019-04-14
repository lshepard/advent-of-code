import re
import sys

def sum_metadata(inpt):
    """Part 1"""
    nodes = list(reversed([int(i) for i in inpt.split(" ")]))
    return sum_metadata_recursive(nodes)[0]

def sum_metadata_recursive(remaining_nodes):
    num_children = remaining_nodes.pop()
    num_metadata = remaining_nodes.pop()

    csum = 0
    for i in range(num_children):
        (child_csum, remaining_nodes) = sum_metadata_recursive(remaining_nodes)
        csum += child_csum
    
    for i in range(num_metadata):
        csum += remaining_nodes.pop()

    return (csum, remaining_nodes)

def value_metadata(inpt):
    """Part 2"""
    nodes = list(reversed([int(i) for i in inpt.split(" ")]))
    return value_metadata_recursive(nodes)[0]
    
def value_metadata_recursive(remaining_nodes):
    num_children = remaining_nodes.pop()
    num_metadata = remaining_nodes.pop()

    child_values = []
    csum = 0

    for i in range(num_children):
        (child_value, remaining_nodes) = value_metadata_recursive(remaining_nodes)
        child_values.append(child_value)
                    
    if num_children == 0:
        for i in range(num_metadata):
            csum += remaining_nodes.pop()
    else:
        # if a node does have child nodes, the metadata entries become indexes
        # which refer to those child nodes. A metadata entry of 1 refers to the
        # first child node, 2 to the second, 3 to the third, and so on. The
        # value of this node is the sum of the values of the child nodes referenced
        # by the metadata entries

        for i in range(num_metadata):
            mvalue = remaining_nodes.pop()
            if len(child_values) >= mvalue:
                csum += child_values[mvalue-1]

    return (csum, remaining_nodes)


if __name__ == "__main__":
    inpt = sys.stdin.read()
    print(value_metadata(inpt))
