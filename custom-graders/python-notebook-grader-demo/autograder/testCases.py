# dependencies
import random, json, sys, random
import numpy as np
from numpy import pi

sys.path.append('solutions/')
from solutions.solutions import factors, rotation_matrix

def createTests(numTestCases):
    # Randomly generate test cases ---------------------------------------------
    # There is a tradeoff in efficiency for generating random/dynamic test cases
    # and solution results each time within the grader. While we adopted this
    # approach for our minimal grader template, we understand that this may not
    # be the best fit for more complex assessments and content.

    # factors tests
    x = [0] + [random.randint(-20,20) for i in range(4)]
    
    # rotation_matrix tests
    y = [random.random()*2*pi for i in range(5)]

    # Compile dictionary. ----------------------------
    testCases = {}
    testCases = {"factors":
                    {"input": x,
                     "output": [factors(j) for j in x]
                    },
                "rotation_matrix":
                    {"input": y,
                     "output": [rotation_matrix(j) for j in y]
                    }
                }

    return testCases
