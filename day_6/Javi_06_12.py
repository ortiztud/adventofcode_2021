# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Import necessary stuff
import time
import os
import sys
from copy import copy
import numpy as np

# Where are we?
os.chdir(os.path.dirname(sys.argv[0]))

# Start ticking
t = time.perf_counter()

# Open input and load it into a where X how much matrix (list of lists)
with open("input.txt") as file_name:
    data = np.loadtxt(file_name, delimiter=",")
    
## Let's go through the list
# Create a copy of the former state to update it
state = copy(data)
for c_day in range(0,80):
    
    new_babies = list()
    for c_fish in range(state.size):
        # Check if a new baby will come out of this fish
        if state[c_fish] == 0:
            new_babies.append(8)
            state[c_fish] = 6
        else: 
            state[c_fish] -= 1
        
    # Include the new guys
    state = np.append(state,new_babies)
    
    # Update
    new_state = copy(state)

# Compute
#print("Hey! Got the answer. It is " + str(len(state)))

print(time.perf_counter()-t)