
# Real Time Color Detection
This Python openCV Color Detector program is developed to detect the defined colors, and display them in a bounding box

## Getting Statrted
First create **Virtual Enviroment** in the directory, each Virtual Enviroment has their own independent set of Python packages installed in their site directories.

Install the Virtual Enviroment by running this command in your terminal
```py
pip install virtualenv
```

Create the Virtual Enviroment using
```py
 python -m venv VirtualEnvironmentName
```

Finally activate the Virtual Enviroment
```py
VirtualEnvironmentName/Scripts/activate
```

### OpenCV
OpenCV is the huge open-source library for **computer vision**, **machine learning**, and **image processing** and now it plays a major role in real-time operation which is very important in today’s systems.

OpenCV can be directly downloaded and installed with the use of pip (package manager).
```py
pip install opencv-python
```

To check if OpenCV is correctly installed, just run the following commands to perform a version check:
```py
import cv2
print(cv2.__version__)
```

### NumPy
NumPy is a general-purpose array-processing package. It provides a high-performance multidimensional array object and tools for working with these arrays. It is the fundamental package for scientific computing with Python. It is open-source software.

Numpy can be installed for Mac and Linux users via the following pip command:
```py
pip install numpy
```

NumPy is commaonly imported as follow:
```py
import numpy as np
```

### Pillow
Python Pillow liberary is built on the top of PIL (Python Image Library) and is considered as the fork for the same as PIL has been discontinued from 2011. Pillow supports many image file formats including BMP, PNG, JPEG, and TIFF.

To install it type the below command in the terminal:
```py
pip install pillow
```

## Calibration
Calibration is the major part of this project, as the visibility of the color in real time is affected by many parameters (i.e camera quality, ambient lighting).
Hence it is important to do the calibration of HSV values first for the required colors.

for the calibration process use the calibration code for HSV value [here](https://github.com/HasnainRaza026/opencv/blob/main/Chapter%207%20(Color%20Detection)/color_detection_webcam.py)


## Demo

https://github.com/HasnainRaza026/Real-Time-Color-Detection/assets/138324430/be3d1788-fbcf-4a2e-b02d-f4781c4ba28c

## Resourses
+ [Murtaza's Workshop](www.youtube.com/@murtazasworkshop)
+ [Pysource](www.youtube.com/@pysource-com)
+ [Computer vision engineer](www.youtube.com/@ComputerVisionEngineer)




