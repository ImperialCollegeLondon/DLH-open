# Converting a .json file from a jupyter notebook into individual programme files

import json, os

def is_package_cell(file_list, package_id):
    # Tests if list of strings provided has the graded function id in the first line

    if (len(file_list) <= 0):
        return False
    first_line = file_list[0]
    return first_line.find(package_id) != -1

def is_graded_cell(file_list, graded_id):
    # Tests if list of strings provided has the graded function id in the first line

    if (len(file_list) <= 0):
        return False
    first_line = file_list[0]
    return first_line.find(graded_id) != -1

def make_submission(nb_output, graded_id, package_id, submission_destination):
    # Creates submissions with the name given after the graded function id in the "submissions" directory
    # Also returns the name of submissions file with correct extension

    with open(nb_output) as f:
        data = json.load(f)

    # Find the file extension to save submission as
    extension = data["metadata"]["language_info"]["file_extension"]

    # Create the file in which the submission will be stored
    file_object  = open(submission_destination+extension, "w+")
    file_object.close

    # For every cell of the original jupyter notebook,
    for i in range(len(data["cells"])):
        # which begins with the package cell identifier
        if is_package_cell(data["cells"][i]["source"], package_id):
            file_list = data["cells"][i]["source"]
        
            # Create text of file
            file_text = ""
            for j in range(len(file_list)):
                file_text += file_list[j]

            # Create the file
            file_object  = open(submission_destination+extension, "a")
            file_object.write(file_text + "\n\n")
            file_object.close()

        # which begins with the graded cell identifier
        elif is_graded_cell(data["cells"][i]["source"], graded_id):
            file_list = data["cells"][i]["source"]
        
            # Create text of file
            file_text = ""
            for j in range(len(file_list)):
                file_text += file_list[j]

            # Create the file
            file_object  = open(submission_destination+extension, "a")
            file_object.write(file_text + "\n    return\n\n")
            file_object.close()

    return "submission"+extension

# This function is provided to generate a solution file based on a model notebook placed
# in the 'model-submission' folder. Feel free to comment it out after using it.

def generate_solution():

    graded_id = '# GRADED'
    package_id = '# PACKAGE'
    generated = 0
    submission_destination = 'autograder/solutions/solutions'

    for file in os.listdir('model-submission/'):
        if file.endswith(".json") or file.endswith(".ipynb"):
            nb_output = file
            make_submission('model-submission/' + nb_output, graded_id, package_id, submission_destination)
            generated += 1
        else:
            nb_output = None
    if generated != 1:
        print('Please place one model notebook in the model-submission directory')
        return

# Comment out this line after using it to generate the model solution in the 'solutions' folder
# generate_solution()