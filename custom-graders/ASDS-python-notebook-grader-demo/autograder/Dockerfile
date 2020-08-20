# Fetch jupyter data-science notebook image
FROM jupyter/datascience-notebook:3b1f4f5e6cc1

RUN fix-permissions /home/jovyan/.jupyter

USER $NB_UID

# conda packages
RUN conda install --quiet --yes \
    'r-corrplot'  \
    'r-doParallel' \
    'r-e1071' \
    'r-expss' \
    'r-foreach'   \
    'r-gbm'   \
    'r-glmnet'    \
    'r-kknn'  \
    'r-neuralnet' \
    # bartmachine dependencies, which install 'foreign' and 'rJava' in their own dependencies
    'r-bartMachineJARs' \
    'r-car' \
    'r-missForest'\
    # jtools dependency
    'r-pander' \
    && \
    conda clean --all -f -y && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

# Packages not in the conda directory require a different command
RUN R -e   "install.packages('bartMachine',   dependencies=TRUE, repos='http://cran.rstudio.com/', quiet = TRUE); \
            install.packages('jtools',        dependencies=TRUE, repos='http://cran.rstudio.com/', quiet = TRUE)"

#USER $NB_USER

WORKDIR "/"
USER root

# Make directories for storing your files.
RUN mkdir /grader
RUN mkdir /grader/solutions

# The commands below copy files into the Docker image.
# Main grader file
COPY grader.py /grader/grader.py
# Helper functions
COPY make_submission.py /grader/make_submission.py
COPY util.py /grader/util.py
COPY testCases.py /grader/testCases.py
# Copy files for the solution

COPY solutions/* /grader/solutions/

# Important: Docker images are run without root access on our platforms. Its important to setup permissions accordingly.
# Executable permissions: Required to execute grader.py
# Read/write permissions: Required to copy over the submission from shared/submission
RUN chmod a+rwx -R /grader/

# Setup the command that will be invoked when your docker image is run.
# Runs 'exec <command>' in WORKDIR. Make sure the first line of the grader file points
# to the location of the programme you wish to execute the command with. For example,
# either '#!/usr/bin/python3' (for Dockerfile which installs python3 at default location)
# or '#!/opt/conda/bin/python3' (for Dockerfile which builds on a jupyter notebook image)
ENTRYPOINT ["grader/grader.py"]
