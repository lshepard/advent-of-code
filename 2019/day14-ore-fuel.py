from collections import defaultdict
import math
from pprint import pprint


class Term:
    def __init__(self, amount, name):
        self.name = name
        self.amount = amount

    def __repr__(self):
        return f"{self.amount}{self.name}"
        
def inpt_graph(inpt):

    # the graph defines how much of any other thing you need
    # to produce the key
    dir_graph = {}
    
    for row in inpt.split("\n"):
        left, right = row.strip().split(" => ")

        amount, name = right.split(" ")

        this_dict = {'amount': int(amount), 'inputs': {}}
        
        for term in left.split(", "):
            tamount, tname = term.split(" ")
            this_dict['inputs'][tname] = int(tamount)

        dir_graph[name] = this_dict
            
    return dir_graph

def ore_required(inpt):
    g = inpt_graph(inpt)
    pprint(g)
    return element_required(g, 'FUEL', 1, 'ORE', 0)

def print_terms(terms, orig_terms, remainders):
    left = ", ".join([f"{v}{k}" for k,v in terms.items()])
    right = ", ".join([f"{v}{k}" for k,v in orig_terms.items() + remainders.items()])
    return f"{left} => {right}"

def element_required(g, desired_element, desired_amount, in_terms_of, level):
    """Attempt at iterative method"""
    print(f"{' ' * level} desired {desired_amount} {desired_element} in terms of {in_terms_of}")

    terms = defaultdict(lambda x: 0)
    remainders = defaultdict(lambda x: 0)

    terms['FUEL'] = 1

    orig_terms = terms
    
    while (True):
        
        print_terms(terms, orig_terms, remainders)
        new_terms = {}
        
        for required_term, required_amount in terms.items():
            # simplify this one
            
            # go through each term and simplify it
            for input_item, input_amount in g[required_term].items():
                new_terms[input_item] += required_amount
                remainders[input_item] += input_amount - required_amount
                
        terms = new_terms
                
def element_required_recursive(g, desired_element, desired_amount, in_terms_of, level):
    """Attempt at recurseive method"""
    print(f"{' ' * level} desired {desired_amount} {desired_element} in terms of {in_terms_of}")
    
    if desired_element == in_terms_of:
        print (f"{' ' * level} returning {desired_amount} {desired_element} ")
        return desired_amount
    else:
        total_in_terms_of = 0
        
        for item, amount in g[desired_element]['inputs'].items():
            received_amount = element_required(g, item, amount, in_terms_of, level+1)
            total_in_terms_of += math.ceil ( desired_amount / received_amount ) * received_amount
            print (f"{' ' * level} adding to total {received_amount} for {amount} {item}")

        print (f"{' ' * level} returning total {total_in_terms_of}")
        return total_in_terms_of

class TestOreFuel():

    def test_input(self):
        test0 = """10 ORE => 10 A
        1 ORE => 1 B"""

        assert inpt_graph(test0) == {'A' : {'amount': 10, 'inputs': {'ORE' : 10}},
                                     'B' : {'amount': 1, 'inputs': {'ORE' : 1}}}

    def test_1(self):
        
        test1 = """10 ORE => 10 A
        1 ORE => 1 B
        7 A, 1 B => 1 C
        7 A, 1 C => 1 D
        7 A, 1 D => 1 E
        7 A, 1 E => 1 FUEL"""
        
        assert ore_required(test1) == 31

    def test_2(self):
        test2 = """9 ORE => 2 A
        8 ORE => 3 B
        7 ORE => 5 C
        3 A, 4 B => 1 AB
        5 B, 7 C => 1 BC
        4 C, 1 A => 1 CA
        2 AB, 3 BC, 4 CA => 1 FUEL"""

        assert ore_required(test2) == 165


    def test_3(self):

        test3 = """157 ORE => 5 NZVS
        165 ORE => 6 DCFZ
        44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
        12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
        179 ORE => 7 PSHF
        177 ORE => 5 HKGWZ
        7 DCFZ, 7 PSHF => 2 XJWVT
        165 ORE => 2 GPVTF
        3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT"""
        
        assert ore_required(test3) == 13312
        
