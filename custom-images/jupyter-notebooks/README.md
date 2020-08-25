# Custom Jupyter Notebooks for Coursera

## Building and testing images locally

- Download the [Coursera labs](https://github.com/coursera/coursera-labs) git repo

- Add any of these folders to the `jupyter` folder

- Follow the Coursera labs instructions to build and run these images locally

## Uploading to Coursera

- Zip the dockerfile

- Add an image, choose to create a custom image, and upload the dockerfile

- Keep the HTTP port as 8888, the default for Jupyter notebook images

- When adding a lab, set the mount point to `/home/jovyan/work`. This is the default location of saved notebooks inside the container. You can use `docker run -it <image_name> sh` in the command line to run an image with a shell to examine the internal file structure to check this for yourself. If your image has an entrypoint you may need `docker run -it --entrypoint sh <image_name>` instead.

# Notes and resources for creating images like these

- [Conda package repo](https://anaconda.org/anaconda/repo)

- [R packages installed by conda](https://docs.anaconda.com/anaconda/packages/r-language-pkg-docs/)

- [R package repo](https://cran.r-project.org/)

- [Python pip package repository](https://pypi.org/) (note that all of these can be installed by pip and are therefore supported in Coursera directly - no need to create a custom image.)

- In general try to install packages from the conda repository before using other sources like the CRAN R repo. This is because there can be version conflict if you do it the other way around.

- For packages in the conda repository, add this to your dockerfile: 

      USER $NB_UID
      RUN conda install --quiet --yes \
      '<package name>' \  
      '<package name 2>' \  
      && \
      conda clean --all -f -y && \
      fix-permissions $CONDA_DIR && \
      fix-permissions /home/$NB_USER
      
- To install other R packages, you can usually use [install.packages()](https://www.rdocumentation.org/packages/utils/versions/3.6.2/topics/install.packages), with

      RUN R -e "<R function 1>; \
                <R function 2>"
             
  - Set “dependencies = NA” for “Depends”, “Imports” and “LinkingTo” dependencies. Using “dependencies = TRUE” includes these and also “Suggests”. Dependencies are only installed if they aren’t already installed - so no duplicates
      
  - “quiet = TRUE” reduces output to make command line output more readable while still useful. In contrast, “verbose = TRUE” can be useful for troubleshooting
  
  - Set repos = ‘http://cran.rstudio.com/’ by default or use a mirror close to the server building the dockerfile, especially if downloading lots of data. Mirrors can be found [here](https://cran.r-project.org/)

