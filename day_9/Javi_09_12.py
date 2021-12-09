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
    
    # Import data as matrix
    # Open input and load it with numpy
    data = list()
    with open("input.txt") as file_name:
         [data.append(x.split().pop()) for x in file_name]
         
    data_num = np.zeros((100, 100))
    for i, val in enumerate(data):
        data_num[i] = [(int(x)) for x in val]
        
        
    # Now I wanna pad with values a frame surrounding the map. I will use the 
    # larger value + 1 for that. Trust me, this will make sense later on.
    max_val = data_num.max() +1
    v_fill = np.ones((1, 100)) * max_val
    h_fill = np.ones((102, 1)) * max_val
    framed = np.vstack ((data_num, v_fill))
    framed = np.vstack ((v_fill,framed))
    framed = np.hstack((framed, h_fill))
    framed = np.hstack ((h_fill,framed))
   
        
    # Function to use a filter-like window to find low points
    def find_low(framed_map, row, col):
        
        # Locate surrounding locations
        adj = list()
        adj.append(framed_map[row-1][col])
        adj.append(framed_map[row][col-1])
        adj.append(framed_map[row][col+1])
        adj.append(framed_map[row+1][col])
        
        # Check if low point
        is_low = framed_map[row][col] < min(adj)
        return is_low
        
    # Call function for every row
    risk_factor = list()
    for i in range(1, len(framed)-1):
        for j in range(1,len(framed)-1):
            if (find_low(framed, i, j)):
                risk_factor.append(framed[i][j] + 1)
            
    
    # # Get answer
    # print("Hey! Got the answer. It is " + str(sum(risk_factor)))
    
    ### Template starts here
    end = time.time()
    
    ## ACTUAL SCRIPT ENDS HERE
    duration.append((end-start)*1000) # append duration of this iteration
    
print("The average time of execution of above program is :", np.mean(duration), "ms")
 
