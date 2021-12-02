import re
import fileinput

lines = list(fileinput.input())

x = 0
y = 0
aim = 0
for line in lines:
    command, num = line.split(" ")
    num = int(num)
    if command == "forward":
        x += num
        y += aim * num
    elif command == "up":
        aim -= num
    elif command =="down":
        aim += num

print(f"x {x} y {y}")
print (x * y)
