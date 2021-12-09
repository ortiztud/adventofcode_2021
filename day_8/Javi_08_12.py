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
import csv

# Where are we?
os.chdir(os.path.dirname(sys.argv[0]))

### Template starts here
duration = list() # create list to append durations of each permutation
for perm in range(1000): # run the script 1000 times to check average duration
    start = time.time()
    
    # Import data and keep only values after |
    data = list()
    with open('input.txt', 'r') as f:
        reader = csv.reader(f, dialect='excel', delimiter='|')
        for row in reader:            
            data.append(row[1].split())
        
    # Function to count number of letters matching our targeted lengths
    def count_letters(digit):
        target_len = [2, 3, 4, 7]
        how_many = 0
        for x in digit:
            if target_len.count(len(x))>0:
                how_many += 1
        return how_many
    
    # Count for every display
    res = list()
    [res.append(count_letters(x)) for x in data]
    
    # Get answer
    print("Hey! Got the answer. It is " + str(sum(res)))
    
    ### Template starts here
    end = time.time()
    
    ## ACTUAL SCRIPT ENDS HERE
    duration.append((end-start)*1000) # append duration of this iteration
    
print("The average time of execution of above program is :", np.mean(duration), "ms")
 
