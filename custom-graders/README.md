# Custom grader images for Coursera labs

This folder contains custom autograders built for Coursera labs images. They use and build upon code from [Coursera's custom grader github repo](https://github.com/coursera/programming-assignments-demo/tree/master/custom-graders). They are run and tested using [courseraprogramming](https://github.com/coursera/courseraprogramming).

## Folder list and descriptions

- `python-notebook-grader-demo` features a grader written for a custom image python notebook in coursera. It is based on `DemoPythonGrader` from [here](https://github.com/coursera/programming-assignments-demo/tree/master/custom-graders), with the addition of a `make-submissions.py` file which converts the user's submission to python files for testing. The grader can be customised for appropriate purposes. More information and detailed instructions for making custom image autograded assigments on Coursera's platform are in the README.

- `ASDS-demo-python-notebook-grader` is almost identical to `demo-python-notebook-grader`, except the Dockerfile is modified to include all of the packages installed in the `ASDS custom notebook image`. The other change is to the first line of the `grader.py` file, which allows the entrypoint of the Dockerfile to execute properly. Since `python-notebook-grader-demo` is likely to be kept more up to date, it's probably better to use this only as assistance if you're struggling to write a grader within a Jupyter notebook image.
