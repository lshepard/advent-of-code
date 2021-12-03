import re
import fileinput
import pandas as pd

lines = list(fileinput.input())

df = pd.DataFrame([list(line.strip()) for line in lines])

m = df.mode()

print(m)
m = "10110"
m = "010111100100"
gamma = ""
epsilon = ""
for i in list(m):
    print("i",i)
    e = (int(i) + 1) % 2
    print("e",e)
    gamma = gamma + str(int(i))
    epsilon = epsilon + str(e)
    
print(int(gamma,2))
print(int(epsilon,2))
print(int(gamma,2) * int(epsilon,2))
