# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Import stuff
import time
import os
import sys
import numpy as np

# Where are we?
os.chdir(os.path.dirname(sys.argv[0]))

### Template starts here
duration = list() # create list to append durations of each permutation
for perm in range(10): # run the script 1000 times to check average duration
    start = time.time()
    
    # Open input and load it with numpy
    with open("input.txt") as file_name:
        data = np.loadtxt(file_name, delimiter=",")
        
    # Let's go through the list (perro way)
    fuel = list()
    for c_pos in range(int(data.max())):
        
        # Compute fuel consumption
        fuel.append(sum(abs(data-c_pos)))
    
    # Get answer
    #print("Hey! Got the answer. It is " + str(min(fuel)))
    
    ### Template starts here
    end = time.time()
    
    ## ACTUAL SCRIPT ENDS HERE
    duration.append((end-start)*1000) # append duration of this iteration
    
print("The average time of execution of above program is :", np.mean(duration), "ms")
 
