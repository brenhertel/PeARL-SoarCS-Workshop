# PeARL SoarCS Workshop
 
Welcome to the PeARL Workshop! Today we will be looking at how robots understand and interact with the world around them! One of the most important peices of understanding the world is vision, so we will be doing some vision processing!

This exercise has 50 images of various color cubes. We will be trying to detect the number of cubes of a certain color in each image, specifically yellow and green. These These images have been taken using a real robot, and are often grainy, have various lighting conditions, and sometimes have camera artifacts. These are issues everyday robots have to work with, and so will you. 

![Example Image](https://github.com/brenhertel/PeARL-SourceCS-Workshop/blob/main/color_cube_detection/data/img61.jpg)

## Step 1: Install Python and OpenCV

If you have not already, you will need to install Python and OpenCV. Do not worry if you are unfamiliar with either of these, we will work through any issues with you!

For installing Python, see here: https://www.python.org/downloads/

One you have Python downloaded, open a terminal and type `python -m pip install numpy opencv-python` (Note: you may have to use `python3 -m pip install numpy opencv-python` instead). Once this finishes, type `python` (or `python3`) in the terminal. This will open up a python scripting environment. In this environment type `import cv2`. If you don't get any errors, you are good to go!

## Step 2: Understanding Color Spaces

Now let's get into the vision processing. A computer typically stores an image as a series of three arrays, each array representing a color channel. The common encoding is RGB (for red, green, blue color channels). OpenCV, however, defies this convention and by default uses BGR, so keep that in mind! Each pixel in an image corresponds to some position in each of these three arrays. For example, a pixel at position (1, 1) could have color value (249, 8, 8), which is a bright red. However, the RGB color space is heavily affected by lighting conditions (shades and tints). For example, the same color but in a darker environment has a value of (107, 4, 4). Still red, but could be confusing with changing lighting conditions. Therefore, we tend to use a different color space, called HSV (for hue, saturation, value color channels). Here, the main value determining color is hue (see here for a representation of RGB and HSV: https://www.rapidtables.com/web/color/color-picker.html). Therefore, we need to primarily find the proper hue values for yellow and green.

One way of checking the color of images is in a file provided, open_image.py. Run this file in command line as: `python open_image.py [image_num] [--hsv]`, where image_num is an odd number from 00-99, corresponding to an image in the data folder, and --hsv is a an optional tag that if specified, will show the HSV color space instead of the BGR color space. When you run this file, click around on a few points in the image. Pixel coordinates and color values will pop up at every point clicked. Use this to find HSV values (lower and upper bounds) for yellow and green cubes. Be careful! The background of these images is also yellowish, so you want to make sure your values don't include the background, otherwise it will be difficult to detect yellow cubes.

## Step 3: Color Filtering, Blurring, and Blob Detection

Once we have good values for a color cube, we need to filter an image for that color. This is done by setting an upper and lower range. All pixels within that range are set to white, and everything outside the range is set to black. This is done using the `cv2.inRange` function. Once filtered, the filtered image (also known as a 'mask') is blurred to reduce noise. A blur is performed by taking a small number of pixels and averaging them together using something called a kernel. This is done for every pixel, and the result is a blurred image. Here, we use a median blur with a kernel of size 5. Finally, we put the blurred image through a blob detector. A blob detector is an algorithm which detects clusters of similar value pixels in an image, here we are using it to detect groups of white pixels, which correspond to our color cubes. The blob detector will return a series of keypoints, one for each blob it finds. 

Note that these three steps are already implemented in count_cubes.py, all you have to do is change the values of the thresholds for yellow and green (lines 5-9). If you wish, you aer welcome to change the blurring and blob detection parameters. Once you have your values in, test using the autograder.py file. Once you have values good enough to get at least 25/50, come see an instructor and we will move onto the next step!

## Step 4: Color Detection on a Real Robot

See an instructor!
