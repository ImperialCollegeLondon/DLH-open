# Custom Images for Coursera Labs

These images utilise `run.sh` to mimic the coursera environment locally when building. This is available in the [Coursera Labs git repo](https://github.com/coursera/coursera-labs).

## Folder list and descriptions

 - The `Docker-101-app` directory contains the files used in the [docker 101 tutorial](https://www.docker.com/101-tutorial) with the addition of a `manifest.json` file, which allows it to be built locally using `run.sh`. It also contains a `README` with some details on how to implement the image in Coursera Labs.

 - Images under the `jupyter-notebooks` directory are built from the base Coursera notebook images. Information for how to build and customise these images can also be found at the [Coursera Labs git repo](https://github.com/coursera/coursera-labs).
