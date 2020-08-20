# dependencies
import random, json, sys

sys.path.append('/solutions/')
from solutions.solutions import factors1, factors2
# from solutions import factors1, factors2

def createTests(numTestCases):
    # Randomly generate test cases ---------------------------------------------
    # There is a tradeoff in efficiency for generating random/dynamic test cases
    # and solution results each time within the grader. While we adopted this
    # approach for our minimal grader template, we understand that this may not
    # be the best fit for more complex assessments and content.

    x = [random.randint(1,10000) for i in range(0,numTestCases)]
    y = [random.randint(1,2000) for i in range(0,numTestCases)]

    # Compile dictionary. partId's are stored here. ----------------------------
    testCases = {}
    testCases = {"factors1":
                    {"input": x,
                     "output": [factors1(j) for j in x]
                    },
                 "factors2":
                    {"input": y,
                     "output": [factors2(j) for j in y]
                    }
                }

    return testCases
