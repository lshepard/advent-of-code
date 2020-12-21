from collections import Counter

import re

inp  = open("inputs/day21").readlines()


amap = dict()

all_ingredients = set()

possibles = set()
counts = Counter()

for line in inp:
    ingredients, allergens = line.split(" (contains ")
    allergens = allergens.strip()[:-1] # cut the trailing paren
    ingredients = set(ingredients.split(" "))
    allergens = allergens.split(", ")
    print(ingredients, allergens)

    for i in ingredients:
        all_ingredients.add(i)
    
    counts.update(ingredients)
    for allergen in allergens:
        amap[allergen] = amap.get(allergen, ingredients)
        amap[allergen]= amap[allergen].intersection(ingredients)


possibles = set()
for allergen, possible_ingredients in amap.items():
    for pi in possible_ingredients:
        possibles.add(pi)

not_present = all_ingredients.difference(possibles)

print("Part 1")
print(sum([counts[n] for n in not_present]))
    
print("part 2")
for key, v in amap.items():
    print(key, v)
print(",".join(sorted(amap.keys())))

# worked out by hand - from the amap
#vfvvnm -> dairy
#bvgm -> eggs
#rdksxt -> fish
#xknb -> nuts
#hxntcz -> peanuts
#bktzrz -> sesame
#srzqtccv -> soy
#gbtmdb -> wheat
