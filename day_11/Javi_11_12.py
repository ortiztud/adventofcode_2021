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
# import matplotlib.pyplot as plt

# Where are we?
os.chdir(os.path.dirname(sys.argv[0]))

### Template starts here
duration = list() # create list to append durations of each permutation
for perm in range(1000): # run the script 1000 times to check average duration
    start = time.time()
    
    # Import data as matrix
    # Open input and load it with numpy
    data = list()
    with open("input.txt") as file_name:
         [data.append(x.split().pop()) for x in file_name]
         
    data_num = np.zeros((10, 10))
    for i, val in enumerate(data):
        data_num[i] = [(int(x)) for x in val]
        
    # I wanna pad with values a frame surrounding the map. I will use the 
    # value 9999 for that. Trust me, this will make sense later on.
    def pad_surr(matrix):
        v_fill = np.ones((1, len(matrix))) * 10
        h_fill = np.ones((len(matrix)+2, 1)) * 10
        framed = np.vstack ((matrix, v_fill))
        framed = np.vstack ((v_fill,framed))
        framed = np.hstack((framed, h_fill))
        framed = np.hstack ((h_fill,framed))
        return framed
    
    # Function to remove the padding
    def remove_pad(matrix):
        matrix = np.delete(matrix, [0,np.shape(matrix)[0]-1],0) # Remove rows
        matrix = np.delete(matrix, [0,np.shape(matrix)[1]-1],1) # Remove cols
        return matrix
    
    # # Function to visualize matrices. Just cause
    # def imagesc(matrix, c_step):
    #     plt.title("Step " + str(c_step))
    #     plt.imshow(matrix)
    
    # Function to get indices for adjacent positions. Gets one position in and 
    # outputs eight adjacent
    def get_adj(row, col):
                
        # Locate surrounding locations.
        adj = list()
        adj.append([row-1,col-1])
        adj.append([row-1,col])
        adj.append([row-1,col+1])
        adj.append([row,col-1])
        adj.append([row,col+1])
        adj.append([row+1,col-1])
        adj.append([row+1,col])
        adj.append([row+1,col+1])
        return adj
    
    # Function to increase activation
    def increase_act(matrix, pos):
        # Pad surroundings
        matrix = pad_surr(matrix)
        
        # Add 1 for the padding
        pos = [(x[0]+1,x[1]+1) for x in pos]
        
        # Loop through positions
        for i in range(len(pos)):
            matrix[pos[i][0],pos[i][1]] = matrix[pos[i][0],pos[i][1]] + 1
            
        # Remove padding
        matrix = remove_pad(matrix)
        
        return matrix
    
    # Stabilize matrix
    def stabilize(matrix):
        ind = matrix >= 10
        ind_list = ind == 9999
        # c = 0
        # While we have still some cells with value 10
        while ind.sum() != 0:
            
        # if ind.sum() !=0:
            # for j in range(1, 3):
            # print("New loop: " + str(c))
            
            # Turn all 9s to 0s
            ind = matrix >= 10
            matrix[ind] = 0
            ind_list = ind | ind_list #Store
            
            # Turn indices into coordinates
            coord = np.nonzero(ind == True)
            # print("The length of coord is " + str(ind.sum()))
            # Spread activation. Loop through all the cells with value 10
            for i in range(len(coord[0])):
                # print("Coord: " + str(coord[0][i]) + str(coord[1][i]))
                # Get adjacent positions for current index
                pos = get_adj(coord[0][i], coord[1][i])
                
                # Increase activation in all of them
                matrix = increase_act(matrix, pos)
                matrix[ind_list] = 0
                # imagesc(matrix,i)
                # print(matrix)
            # c += 1
        # imagesc(matrix,999)
        n_flash = ind_list.sum()
        out = (matrix, n_flash)
        return out
    
    # Create a copy
    mat = data_num
    tot_flash = 0
    for i in range(100):
        temp = stabilize(mat+1)
        mat = temp[0]
        tot_flash = temp[1] + tot_flash
    
    
    # Get answer
    # print("Hey! Got the answer. It is " + str(tot_flash))
    
    ### Template starts here
    end = time.time()
    
    ## ACTUAL SCRIPT ENDS HERE
    duration.append((end-start)*1000) # append duration of this iteration
    
print("The average time of execution of above program is :", np.mean(duration), "ms")
 
