# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Import necessary stuff
import time
import os
import sys

# Where are we?
os.chdir(os.path.dirname(sys.argv[0]))

# Start ticking
t = time.perf_counter()

# Open input and load it into a where X how much matrix (list of lists)
with open("input.txt",'r') as f:
    data = [x.split() for x in f.readlines()]
    f.close()

# Let's navigate!
horiz = 0
vert = 0
for ind, value in enumerate(data):
    if value[0] == 'forward':
        horiz += int(value[1])
    elif value[0] == 'down':
        vert += int(value[1])
    elif value[0] == 'up':
        vert -= int(value[1])
   
print("Hey! Got the answer. It is " + str(horiz*vert))
print(time.perf_counter()-t)

# Fancier but slightly slower
# t = time.perf_counter()
# def get_values(data, direction):
#     c=list()
#     [c.append(int(value[1])) for i, value in enumerate(data) if value[0] == direction]
#     return c

# # Compute
# horiz = sum(get_values(data, "forward"))
# vert = sum(get_values(data, "down")) - sum(get_values(data,"up"))
# print("Hey! Got the answer. It is " + str(horiz*vert))
# print(time.perf_counter()-t)
