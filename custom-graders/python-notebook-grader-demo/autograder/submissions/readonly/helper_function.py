## This file is an external helper function for the graded notebook.
# The notebook expects the file to be under the readonly folder in the same directory as the notebook.
# Include the readonly folder and this file in the solutions and submissions folders.
# This allows the dockerfile to include it in the correct places for the autograder to run correctly.


# A function to test if the given input is a positive integer.

def is_pos_int(n):
    
    try:
        if float(n).is_integer() and n>0:
            return True
        else:
            return False
    except:
            return False