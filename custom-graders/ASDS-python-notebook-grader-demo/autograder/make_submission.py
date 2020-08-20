# Converting a .json file from a jupyter notebook into individual programme files

import json, os

def is_graded_function(file_list, graded_id):
    # Tests if list of strings provided has the graded function id in the first line

    if (len(file_list) <= 0):
        return False
    first_line = file_list[0]
    return first_line.find(graded_id) != -1

def make_submission(nb_output, graded_id, submission_destination):
    # Creates submissions with the name given after the graded function id in the "submissions" directory
    # Also returns the name of submissions file with correct extension

    with open(nb_output) as f:
        data = json.load(f)

    # Find the file extension to save submission as
    extension = data["metadata"]["language_info"]["file_extension"]

    # Create the file in which the submission will be stored
    file_object  = open(submission_destination+"submission"+extension, "w+")
    file_object.close

    # For every cell of the original jupyter notebook,
    for i in range(len(data["cells"])):
    # which begins with the graded function identifier
        if is_graded_function(data["cells"][i]["source"],graded_id):
            file_list = data["cells"][i]["source"]
        
            # Create text of file
            file_text = ""
            for j in range(len(file_list)):
                file_text += file_list[j]

            # Create the file
            file_object  = open(submission_destination+"submission"+extension, "a")
            file_object.write(file_text + "\n    return\n\n")
            file_object.close()

    return "submission"+extension