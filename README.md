# UAV-Image-Processing-Computer
The software to be run on the aerial vehicle's image processing computer (i.e. Nvidia Jetson Nano)  

This branch contains the initial image processing work done over the summer of 2021. 

## Main Focus
The goal of this summer work is to determine the best process for creating a program to isolate and identify regions of intrest from aerial photographs. The competition requires idetification of polygons with alphanumerics in the ceter as well as people on the ground. This branch primarily focuses on isolation and recognition of the polygons.

## Inital setup
Opencv will be used for the inital image processing and tensorflow for creating models specific to isolating areas of intrest.
In order to make these programs portable between different computers a docker container is used to setup an envrioment with the dependencies for opencv and tensorflow. 

In order to spin up this container docker is required, follow the install instructions for your system on the docker installation guide.
> https://docs.docker.com/get-docker/
###### Note
On windows WSL is required for both installation and to spin up the following containers if you are running windows. 
GPU support may require a some machine specfic instructions on install, I recommend going through this process as programs will run significantly faster. For nvidia gpus refrence the following.
> https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html

TODO: add for AMD gpus, will require a bit more work as there isn't much documentation 

Once docker is installed clone this repository and checkout this branch on your machine. Navigate to the UAV-Image-Processing-Computer repository and use the following command in the terminal to build one of the docker containers. This will not work without using sudo with this command. Replave (NAME) with what you want this container to be named.
###### CPU only
```
docker build -t NAME .
```
###### GPU
```
docker build -t NAME:gpu . 
```

## Accessing the training data
The training data for this project is stored in the shared UAVND Files google drive in the following folder. 
>UAVND Files/Media/Training Data/Summer 2021
The fastest way to download this data is to download the whole Summer 2021 folder and move it into the directory containing this repository on your machine. 
Additonally, you can use the command line to download these images. Move the Summer 2021 folder from the shared UAVND Files drive into your personal google drive. Then install gshell and download with the following commands from the directory containing this this repository.
```
pip install gshell
gshell init
gshell download Summer\ 2021
```

## Running programs
To run these programs use the following commands to spin up a docker container and allow for shell interation within the container. 
```
TODO docker run command 
```

## Initial Progress
So far the isolate.py program takes an image and uses filters and gradient edge detection in opencv to outline regions that are significantly different from the local background of that area. 

TODO add images from this program running

The next steps are to label regions of interest in the images after isolate.py (or a similar program that you design) has been run on the training data, and then use tensorflow to isolate these areas of intrest. 

From here I think adapting a pretrained polygon or alphanumeric recognition model to our usecase is probably the easiest solution. The refrences section has links to a few opensource programs but feel free to explore for ones that better fit the project. 

## Resources
Documentation
>OpenCV:
>https://docs.opencv.org/master/d6/d00/tutorial_py_root.html
>
>Tensorflow:
>https://www.tensorflow.org/install/docker
>
>Docker:
>https://docs.docker.com

Opensource text/shape recognition programs
>https://github.com/Lydorn/polycnn
>https://github.com/tensorflow/models/tree/master/research/object_detection
>https://www.pyimagesearch.com/2018/09/17/opencv-ocr-and-text-recognition-with-tesseract/


