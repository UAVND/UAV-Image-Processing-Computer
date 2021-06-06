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

As of right now only nvidia gpus work with this docker container.

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
To run these programs use the following commands to spin up a docker container and allow for shell interation within the container. Replace "/pathToFolderWithTrainingData" with the path to the folder on your machine that contains the training data. Replace "NAME:tag" with the name used in the initial setup step and "tag" with "latest" if using CPU only and "gpu" if using GPU version.  
```
docker run /pathToFolderWithTrainingData:/home/TrainingData -it NAME:tag bash
```

## Initial Progress
So far the isolate.py program takes an image and uses filters and gradient edge detection in opencv to outline regions that are significantly different from the local background of that area. 

Original image:
![image](https://user-images.githubusercontent.com/61067101/120911684-38a93600-c657-11eb-8e35-8b08b7243316.png)

After processing:
![image](https://user-images.githubusercontent.com/61067101/120911670-19aaa400-c657-11eb-92fc-394c5a626cea.png)

The next steps are to label regions of interest in the images after isolate.py (or a similar program that you design) has been run on the training data, and then use tensorflow to isolate these areas of intrest. 

From here I think adapting a pretrained polygon or alphanumeric recognition model to our usecase is probably the easiest solution. The refrences section has links to a few opensource programs but feel free to explore for ones that better fit the project. 

## General Comments
The docker container has both tensorflow and opencv installed. It will allow you to run scripts that use both as well as there dependcies. Without machine specific setup there is not an effcient way to pipe GUI output to your machine so when running programs in the docker container save them to the working directory and view them later on your machine. 

Upon start up the docker container will give you a warning that you are in root mode, this is necessary as I haven't found a good way to give the container write permissions to the local machine without running in root mode. That said, be careful as files created and deleted inside the docker container will impact your machine outside of the container. (If you can figure at a way to pass write permission through to docker without running in root mode feel free to update the Dockerfiles above)

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


