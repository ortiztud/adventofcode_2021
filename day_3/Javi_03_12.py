# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Import necessary stuff
import time
import os
import sys
from statistics import mode
# import numpy as np

# Where are we?
os.chdir(os.path.dirname(sys.argv[0]))

# Start ticking
t = time.perf_counter()

# Open input and load it into a where X how much matrix (list of lists)
# data = np.loadtxt("input.txt", dtype=str)

# count = np.count_nonzero(data == 1, axis=1)

with open("input.txt",'r') as f:
    data = [list(x.split()[0]) for x in f.readlines()]
    f.close()

# Transpose
data_t = list(zip(*data))

# Get mode
gamma = list()
[gamma.append(mode(x)) for x in data_t]

# Turn string binary into decimal 
gamma_str = ""
gamma_str = gamma_str.join(gamma)
gamma_rate = int(gamma_str,2)

# Inverse gamma
epsilon = list()
[epsilon.append(str((int(x)-1)*-1)) for x in gamma]

# Turn string binary into decimal 
epsilon_str = ""
epsilon_str = epsilon_str.join(epsilon)
epsilon_rate = int(epsilon_str,2)

# Compute
print("Hey! Got the answer. It is " + str(gamma_rate*epsilon_rate))
print(time.perf_counter()-t)


