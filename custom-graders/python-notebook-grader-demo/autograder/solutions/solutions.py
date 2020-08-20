# PACKAGE CELL
import numpy as np
from numpy import pi
from readonly.helper_function import is_pos_int

# GRADED FUNCTION: factors

def factors(n):
    
    factors_list = []
        
    if is_pos_int(n):
    ### WRITE YOUR CODE HERE
        factors_list = [i for i in range(1,n) if n%i == 0] + [n]
    ### END OF LEARNER CODE
    
    return factors_list
    return

# GRADED FUNCTION: rotation_matrix

def rotation_matrix(theta):
    
    ### Complete the definitions of c and s here
    c = np.cos(theta)
    s = np.sin(theta)
    ### END OF LEARNER CODE
    
    return np.array(((c,-s),(s,c)))
    return

