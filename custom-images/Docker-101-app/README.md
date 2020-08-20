# Docker-101-app

The files available in the [docker-101 tutorial](https://www.docker.com/101-tutorial), with the addition of the manifest.json file needed to test locally using [run-lab](https://github.com/coursera/coursera-labs).

In order to implement the image in Coursera:

 - When adding a custom image on Coursera, choose the HTTP port that the app will be listening on. For the docker-101 todos app, this is `port 3000`.
 
 - The mount point for individual labs should be the file location inside the image where you would attach a volume. Files under this directory will be stored on Coursera servers when the lab isn’t open. For the docker-101 todos app, this is `/etc/todos`

## Some further notes:

 - Use Coursera's [run-lab](https://github.com/coursera/coursera-labs) to test viability of apps inside coursera framework. 

 - A manifest.json file is required for local building of an image, but it is not necessary when uploading the final .zip of the file system to Coursera.

 - Make sure the Dockerfile is at the root of the compressed directory when uploading to coursera

 - [Docker Hub](https://hub.docker.com/search?q=&type=image) of base images from which to build your app. Eg. node for javascript environment.
