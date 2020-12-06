#!/bin/bash

# Preprocess: we need to take the input and put each group onto its own line
# We use sed to add a space to empty lines,
# then tr to replace each newline with a # (this compresses each group into its own line)
# finally sed to remove the leading # so that the number of # is a good count
sed 's/^$/ /g' <&0 | tr \\n "#" | egrep -o '[#a-z]+' | sed "s/^#//" > boarding_groups

# then for each boarding group, split characters into their own line, then sort uniq to dedupe and finally count
# use paste/bc to add up all the numbers that come out
echo "Part 1:"
for g in `cat boarding_groups`; do echo $g | egrep -o "[^#]" | sort | uniq | wc -l ; done | paste -sd+ - | bc

# part 2 was harder to do in a single line - so it's two steps
# first, count the number of # (this is the number of individual passengers in the group)
# then, count how many of each answer - and use awk to print it only if the count equals the total passengers
# count those lines with wc
# finally add them all up with paste/bc one-liner
echo "Part 2:"
for g in `cat boarding_groups`; do
  NUM=`echo $g | egrep -o "\#" | wc -l`
  echo $g | egrep -o "[^#]" | sort| uniq -c | awk -v total="$NUM" '{if ($1 == total) {print $1}}' | wc -l
done | paste -sd+ - | bc

