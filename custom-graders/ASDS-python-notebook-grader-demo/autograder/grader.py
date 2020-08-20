#!/opt/conda/bin/python3

# ^^^ ENTRYPOINT for Dockerfile

# Dependencies
import sys, os, stat, shutil

# Import helper functions from util.py, and testCases.py
from util import print_stderr, send_feedback, stdout_redirected
from make_submission import make_submission
from testCases import createTests

def main():
    # Define # of test cases per code block and # of graded code blocks -------------------------------------
    # Please ensure that the numTestCases and numGradedFuncs are integers >= 1.
    numTestCases = 5
    numGradedFuncs = 2

    if numTestCases >= 1 and float(numTestCases).is_integer() and numGradedFuncs >= 1 and float(numGradedFuncs).is_integer():
        testCasePenalty = 1.0/(numTestCases*numGradedFuncs)
    else:
        print_stderr("Please check that numTestCases and numGradedFuncs are whole integers greater than 0.")
        send_feedback(0.0, "Please reach out to course staff via discussion forums, to report a grader error.")
        return

    # Find the learner's submission and create appropriate file ----------------------------------------------

    # The directory /shared/submission/ is the standard submission directory across all courses.
    # This is a readonly directory. If you'd like the students to submit a zip with multiple files,
    # please ensure that the grader first moves the files to a folder with the correct permissions to unzip.

    submission_location = "/shared/submission/"

    # Set identifier for output file and graded code
    graded_id = "# GRADED FUNCTION:"
    submission_destination = "/grader/" #"submissions/"

    for file in os.listdir(submission_location):
        if file.endswith(".json"):
            nb_output = file
        else:
            nb_output = None
    if nb_output is None:
        send_feedback(0.0, "Please reach out to course staff via discussion forums, to report a grader error.")
        return

    # Converts notebook output to submission.<extension> and saves in /grader/ folder, which has executable permissions
    try:
        make_submission(submission_location + nb_output, graded_id, submission_destination)
    except Exception as e:
        print_stderr("make_submission returned this error: " + str(e))
        send_feedback(0.0, "Please reach out to course staff via discussion forums, to report a grader error.")
        return

    # Generate test cases ------------------------------------------------------
    try:
        testCases = createTests(numTestCases)
    except Exception as e:
        print_stderr("createTests returned this error: " + str(e))
        send_feedback(0.0, "Please reach out to course staff via discussion forums, to report a grader error.")
        return

    # Run the learner submission -----------------------------------------------

    # import learner graded functions
    sys.path.append(submission_destination)
    try:
        from submission import factors1, factors2
    except Exception as e:
        send_feedback(0.0, "Your code returned this error: " + str(e))
        return

    # Number of test cases failed.
    numTestCasesFailed = 0

    # Specific feedback flags
    factors1_feedback = 0
    factors2_feedback = 0

    try:
        #stdout_redirected prevents print statements from learner submission
        #from being stored in stdout
        with stdout_redirected():
            learnerOutput = [factors1(x) for x in testCases["factors1"]["input"]]
    except Exception as e:
        send_feedback(0.0, "Your code returned this error: " + str(e))
        return

    for j in range(0,numTestCases):
        if testCases["factors1"]["output"][j] != learnerOutput[j]:
            numTestCasesFailed += 1
            factors1_feedback = 1

    try:
        #stdout_redirected prevents print statements from learner submission
        #from being stored in stdout
        with stdout_redirected():
            learnerOutput = [factors2(x) for x in testCases["factors2"]["input"]]
    except Exception as e:
        send_feedback(0.0, "Your code returned this error: " + str(e))
        return

    for j in range(0,numTestCases):
        if testCases["factors2"]["output"][j] != learnerOutput[j]:
            numTestCasesFailed += 1
            factors2_feedback = 1

    # Calculate score and send feedback ----------------------------------------
    totalPenalty = min(1.0, (testCasePenalty*numTestCasesFailed))
    finalFractionalScore = 1.0 - totalPenalty

    if numTestCasesFailed > 0:
        feedback = "Your solution failed " + str(numTestCasesFailed) + " out of " + str(numGradedFuncs*numTestCases) + " test cases."
        if factors1_feedback:
            feedback += " Test case(s) failed in factors1."
        if factors2_feedback:
            feedback += " Test case(s) failed in factors2."
        feedback += " Please try again!"
    else:
        feedback = "Great job! You passed all test cases."
    send_feedback(finalFractionalScore,feedback)

if __name__ == '__main__':
    main()
