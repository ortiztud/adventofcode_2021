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

# Where are we?
os.chdir(os.path.dirname(sys.argv[0]))

### Template starts here
duration = list() # create list to append durations of each permutation
for perm in range(10): # run the script 1000 times to check average duration
    start = time.time()
    
    # Import data
    data = list()
    with open("input.txt") as f:
        data = [x.split() for x in f.readlines()]
    
    '''
    First thing, let's get rid of the initial inputs since these are reserved characters
    when handling strings.
    
    I will use the following conversion table:
        () becomes ab
        [] becomes cd
        {} becomes ef
        <> becomes gh
    '''
    table = list()
    table.append(("(", "a"))
    table.append([")", "b"])
    table.append(["[", "c"])
    table.append(["]", "d"])
    table.append(["{", "e"])
    table.append(["}", "f"])
    table.append(["<", "g"])
    table.append([">", "h"])

    def convert_chars(input_data, table):
        for c_char, val in enumerate(table):
            for c_lines, val2 in enumerate(input_data):
                input_data[c_lines][0] = input_data[c_lines][0].replace(table[c_char][0],table[c_char][1])
        return input_data
    
    data = convert_chars(data, table)
    
    # Characters
    open_char = ('a','c','e','g')
    close_char = ('b','d','f','h')
        
    # Function to count number of openning and closing characters in a string
    def n_chars(sub_snip, targ_char):
        
        # Characters
        open_char = ('a','c','e','g')
        close_char = ('b','d','f','h')
    
        sub_snip = sub_snip + targ_char

        # Count closing chars
        c_num = list()
        o_num = list()
        [c_num.append(sub_snip.count(x)) for x in close_char]
        [o_num.append(sub_snip.count(x)) for x in open_char]
        # print(c_num)
        # print(o_num)
        return [sum(o_num), sum(c_num)]
        
    # Function to chop the string into 0-closing char substrings
    def get_snippets(line, targ_char):
        pos = [x.start() for x in re.finditer(targ_char, line)]
        
        snippets = list()                                      
        for i, val in enumerate(pos):
            snippets.append(line[0:val])
        
        return snippets
    
    # Function that gets a line, a set of opening chars and a target closing char
    # and returns the first illegal position
    def get_illegal_pos(line, open_targ, targ_char):
        illegal_pos = list()
        illegal_char = list()
        is_corrupt = 0
        
        # Get snippets
        snippets = get_snippets(line[0], targ_char)
        
        # Loop through possible snippets and stop at first
        for k, val in enumerate(snippets):
            # If the number of openning targ_char is smaller than the number
            # of closing ones, this is corrupt.
            if val.count(open_targ) < k+1:
                # illegal_char.append(targ_char)
                illegal_pos.append(len(val))
                is_corrupt = 1
                print("Corrupt")
                break
            # Now I want to take this snippet and look up the last opening targ_char
            # as an index to get the full sequence of characters between the opening
            # ans closing.
            else :
                st_ind = [x.start() for x in re.finditer(open_targ, val)]
                st_ind = st_ind[::-1]
                
                sub_snip = val[st_ind[k]:]
                # If there's only one, we can move on.
                if len(sub_snip) != 1:
                    how_many = n_chars(sub_snip, targ_char)
                    # If number of opening is larger than number of closing
                    # then it is corrupt
                    if how_many[0]>how_many[1]:
                        # illegal_char.append(targ_char)
                        illegal_pos.append(len(val))
                        is_corrupt = 1
                        print("corrupt!")
                        # print(illegal_pos)
                        break
                    elif how_many[0]<how_many[1]:
                        # print("It will be corrupt but not yet")
                        print("")
                    elif how_many[0] == how_many[1]:
                        # print("same number. all clear here")
                        print("")
                        
                    
        
        # Output
        if is_corrupt:
            return illegal_pos
        else: 
            return 9999
    
    # Which one was first?
    def which_first(line, close_char):
        print("Starting...")
        temp=list()
        for i, val in enumerate(close_char):
            temp.append(get_illegal_pos(line, open_char[i], val))
        if min(temp) !=9999:
            first_ill = line[0][min(temp)[0]]
            print(first_ill)
            return first_ill
        else:
            print("Incomplete")
    # which_first(data[0], close_char)
    
    # Use function to all lines in data
    all_illegal = list()
    for i, val in enumerate(data):
        all_illegal.append((which_first(val, close_char)))
    
    
    
            
    #     # Locate surrounding locations
    #     adj = list()
    #     adj.append(framed_map[row-1][col])
    #     adj.append(framed_map[row][col-1])
    #     adj.append(framed_map[row][col+1])
    #     adj.append(framed_map[row+1][col])
        
    #     # Check if low point
    #     is_low = framed_map[row][col] < min(adj)
    #     return is_low
        
    # # Call function for every row
    # risk_factor = list()
    # for i in range(1, len(framed)-1):
    #     for j in range(1,len(framed)-1):
    #         if (find_low(framed, i, j)):
    #             risk_factor.append(framed[i][j] + 1)
            
    
    # # Get answer
    # print("Hey! Got the answer. It is " + str(sum(risk_factor)))
    
    ### Template starts here
    end = time.time()
    
    ## ACTUAL SCRIPT ENDS HERE
    duration.append((end-start)*1000) # append duration of this iteration
    
print("The average time of execution of above program is :", np.mean(duration), "ms")
 
