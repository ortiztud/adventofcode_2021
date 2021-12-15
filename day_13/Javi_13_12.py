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
import re
import matplotlib.pyplot as plt

# Where are we?
os.chdir(os.path.dirname(sys.argv[0]))

### Template starts here
duration = list() # create list to append durations of each permutation
for perm in range(1000): # run the script 1000 times to check average duration
    start = time.time()
    
    # Import data as matrix
    # Open input and load it line by line
    data = list()
    with open("input2.txt") as f:
        [data.append(x.split("\,")) for x in f]
        
    # Look up where folding instructuions start a split data
    for i, val in enumerate(data):
        if val[0] == "\n":
            data_num = data[0:i]
            inst =data[i+1:]
            break
    
    def invert_y_pos(y_pos):
        max_val = y_pos.max()
        inv_pos = np.zeros((len(y_pos),1))
        for i, val in enumerate(y_pos):
            inv_pos[i] = max_val - val
            
        return inv_pos
    
    # Turn input into numbers
    col_input = np.zeros((len(data_num), 1))
    row_input = np.zeros((len(data_num), 1))
    for i, val in enumerate(data_num):
        row_input[i] = int(val[0].split(",")[1])
        col_input[i] = int(val[0].split(",")[0])
    
    # Invert y axis
    row_input = invert_y_pos(row_input)
    map_input = np.concatenate((row_input, col_input), axis = 1)
    # Function to visualize matrices. Just cause
    def imagesc(matrix):
        plt.imshow(matrix)
        
    # Print list of signaled locations
    dim = map_input.max(0)
    paper = np.zeros((int(dim[0]), int(dim[1])))
    for i, val in enumerate(map_input):
        paper[int(val[0])-1,int(val[1])-1] = 1
        
    # Get folding instructions into a proper format
    inst_form = list()
    [inst_form.append(x[0].split("=")) for x in inst]
    axes = list()
    where_to_fold = list()
    for i, val in enumerate(inst_form):
         axes.append(val[0][-1])
         where_to_fold.append(int(val[1]))
    
    # Function to get coord info
    def get_coord_info(paper, axis, where):
         # Locate puntos
        ind = paper == 1
        all_coord = np.nonzero(ind == True)
        
        if axis == 'x':
            coord_ind = 1
        elif axis == 'y':
            coord_ind = 0
            
        # How many lines after fold
        how_many_after_fold = sum(all_coord[coord_ind]>where)
        
        # Puntos to change
        ind_to_change = all_coord[coord_ind] > where
        coord_to_change = np.nonzero(ind_to_change == True)
        
        # Output
        out = [all_coord, how_many_after_fold, coord_to_change]
        return out
    
     # Function to fold
    def fold(paper, axis, where):
        # Loop through all the puntos after the fold
        info = get_coord_info(paper, axis, where)
        all_coord = info[0]
        coord_to_change = info[2]
        for i in range(info[1]):
            
            # Get original positions
            col_coord = all_coord[1][coord_to_change[0][i]]
            row_coord = all_coord[0][coord_to_change[0][i]]
            

            if axis == 'x':
                # How much to fold
                dist_to_fold = col_coord - where
                # Update coords
                row_coord = row_coord # Does not change when folding on x
                col_coord = col_coord - dist_to_fold*2
                
                # Remove everything after fold
                paper[:][where:] = 0
                
            elif axis == 'y':
                # How much to fold
                dist_to_fold = row_coord - where
            
                 # Update coords
                row_coord = row_coord - dist_to_fold*2
                col_coord = col_coord # Does not change when folding on y
                
                # Remove everything after fold
                paper[where:][0] = 0
                
            # Print new punto
            # print(dist_to_fold)
            paper[row_coord][col_coord] = 1

        return paper
    
    # Loop through instructions
    for i in range(1):
        print("Instruction " + str(i+1))
        paper = fold(paper, axes[i], where_to_fold[i])
    
    
    # Get answer
    print("Hey! Got the answer. It is " + str(paper.sum()))
    adfadad
    ### Template starts here
    end = time.time()
    
    ## ACTUAL SCRIPT ENDS HERE
    duration.append((end-start)*1000) # append duration of this iteration
    
print("The average time of execution of above program is :", np.mean(duration), "ms")
 
