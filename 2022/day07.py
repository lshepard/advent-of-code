import fileinput
import textwrap
import re

lines = list(fileinput.input())

# parse the input commands

# let's try to keep directories and files separate.
# files - just a list by filename of the size of each file
# directories - each directory, and a list of what it contains, whether file or dir.

def parse_lines_for_files(lines):
    files = {}
    path = []
    
    for line in lines:
        line = line.strip()
        if (line == "$ cd .."):
            # move back a directory
            path.pop()
        elif (line == "$ cd /"):
            path = []
        elif (m := re.match("\$ cd (\w+)", line)):
            # move into a directory
            target = m[1]
            path.append(target)
        elif (m := re.match("(\d+) ([a-z.]+)", line)):
            # read a file's info
            name = "/" + "/".join(path + [m[2]])
            size = m[1]
            if name in files:
                raise Exception("file {name} already exists")
            files[name] = int(size)
        elif (line == "$ ls"):
            pass # ignore
        elif (m := re.match("dir ([a-z.]+)", line)):
            pass # ignore for now
        else:
            raise Exception(f"Unknown command: {line}")

    return files
        
def directory_sizes(files):
    # iterate through each file, adding its size to
    # the total for all the directories it contains
    dir_sizes = {}
    for name, size in files.items():
        # f like "/a/b/blah"
        for d in directory_names(name):
            if not d in dir_sizes:
                dir_sizes[d] = 0
            dir_sizes[d] += size

    return dir_sizes

def directory_names(file_name):
    """All the directories that contain this file. let's do fully qualified"""

    start = 0
    dirs = []
    while True:
        i = file_name.find("/", start)
        if i == -1:
            break
        dirs.append(file_name[:i])
        start = i+1
    return dirs

def part1_total(sizes):
    """find all of the directories with a total size of at
        most 100000, then calculate the sum of their total sizes"""
    s = [v for k,v in sizes.items() if v <= 100000]
    return sum(s)

def part2_total(sizes):
    """Find the smallest directory that, if deleted, would free up 
    enough space on the filesystem to run the update.
    The total disk space available to the filesystem is 70000000. 
    To run the update, you need unused space of at least 30000000."""
    total = sizes[""]
    unused = 70000000 - total
    print(f"unused {unused}")
    needed = 30000000 - unused
    print(f"needed {needed}")
    return min([v for k,v in sizes.items() if v >= needed])

def print_files(files):
    for f, size in files.items():
        print(f"{size}\t{f}")
        
files = parse_lines_for_files(lines)
print_files(files)
sizes = directory_sizes(files)
    
for s, d in (sorted([(s, d) for d, s in sizes.items()])):
    print(f"{s}\t{d}")
print(f"pt1: {part1_total(sizes)}")

print(f"pt2: {part2_total(sizes)}")
