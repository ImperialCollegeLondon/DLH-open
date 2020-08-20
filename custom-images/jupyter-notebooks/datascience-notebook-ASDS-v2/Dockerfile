FROM jupyter/datascience-notebook:3b1f4f5e6cc1

RUN fix-permissions /home/jovyan/.jupyter

USER $NB_UID

# conda packages
RUN conda install --quiet --yes \
    'r-autoencoder' \
    'r-corrplot'  \
    'r-doParallel' \
    'r-e1071' \
    'r-expss' \
    'r-foreach'   \
    'r-gbm'   \
    'r-glmnet'    \
    'r-kknn'  \
    'r-neuralnet' \
    'r-rpart.plot' \
    # EnsemblePCReg dependencies, which install 'foreign' and 'rJava' in their own dependencies
    'r-bartMachineJARs' \
    'r-car' \
    'r-missForest'\
    # jtools dependency
    'r-pander' \
    # ResourceSelection dependency
    'r-pbapply' \
    && \
    conda clean --all -f -y && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

# Packages not in the conda directory require a different command
RUN R -e   "install.packages('EnsemblePCReg',   dependencies=TRUE, repos='http://cran.rstudio.com/', quiet = TRUE); \
            install.packages('ResourceSelection',   dependencies=TRUE, repos='http://cran.rstudio.com/', quiet = TRUE); \
            install.packages('jtools',        dependencies=TRUE, repos='http://cran.rstudio.com/', quiet = TRUE)"

USER $NB_USER