# PeARL SourceCS Workshop
 
Welcome to the PeARL Workshop! Today we will be looking at how robots understand and interact with the world around them! One of the most important peices of understanding the world is vision, so we will be doing some vision processing!

This exercise has 50 images of various color cubes. We will be trying to detect the number of cubes of a certain color in each image, specifically yellow and green. These These images have been taken using a real robot, and are often grainy, have various lighting conditions, and sometimes have camera artifacts. These are issues everyday robots have to work with, and so will you. 

## Step 1: Install Python and OpenCV

If you have not already, you will need to install Python and OpenCV. Do not worry if you are unfamiliar with either of these, we will work through any issues with you!

For installing Python, see here: https://www.python.org/downloads/

One you have Python downloaded, open a terminal and type `python -m pip install numpy opencv-python` (Note: you may have to use `python3 -m pip install numpy opencv-python` instead). Once this finishes, type `python` (or `python3`) in the terminal. This will open up a python scripting environment. In this environment type `import cv2`. If you don't get any errors, you are good to go!

