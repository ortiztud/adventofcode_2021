# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Import necessary stuff
import time
import os
import sys

# Start ticking
t = time.perf_counter()

# Where are we?
os.chdir(os.path.dirname(sys.argv[0]))

# Open input and turn it into integers
f = open("input.txt", "r")
data = f.read().split()
f.close()
data = list(map(int,data))

# Counter
count = 0

# Let's loop!
for ind in range(1,len(data)):
    if data[ind]>data[ind-1]:
        count +=1
        
#print("Hey! Got the answer. It is " + str(count))
print(time.perf_counter()-t)
