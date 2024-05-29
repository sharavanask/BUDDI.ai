# README

## Image Matching with 2D Convolution

This project implements a simple image matching algorithm using 2D convolution. The goal is to find the position of a cropped part within a full image. The result is visualized by drawing a rectangle around the matched region.

### Files

- `imagecon.py`: This script contains the functions to load, normalize, and perform 2D convolution on the images, and to visualize the result.
- `README.md`: This file provides an overview and instructions for running the script.

### Requirements

- Python 3.x
- NumPy
- TensorFlow
- Matplotlib

# Functions

# convolve2d(image, kernel)
This function performs a 2D convolution between the input image and the kernel (cropped part). It returns the convolution result.

# Usage
Define the paths for the full image and the cropped part.
Load the images using the load_image function.
Normalize the images using the normalize function.
Perform 2D convolution using the convolve2d function.
Find the position of the highest value in the convolution result, indicating the top-left corner of the matched region.
Draw a rectangle around the matched region (optional).
Display the original image and the image with the detected match using Matplotlib.

# Output Images of Full and Detected image

![Full](https://github.com/sharavanask/BUDDI.ai/blob/main/Day%209%20Image%20Convolution/inputimg.png)
![Cropped](https://github.com/sharavanask/BUDDI.ai/blob/main/Day%209%20Image%20Convolution/imageposition.png)
