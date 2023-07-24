#from https://www.geeksforgeeks.org/displaying-the-coordinates-of-the-points-clicked-on-the-image-using-python-opencv/

import cv2
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Open image file for querying.')
parser.add_argument('image_num', help='image query number')
parser.add_argument('--hsv', action='store_true', help='if specified shows hsv instead of bgr encoding')

args = parser.parse_args()
print(args.image_num, args.hsv)


# function to display the coordinates of
# of the points clicked on the image 
def click_event(event, x, y, flags, params):
  
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
  
        # displaying the coordinates
        # on the Shell
        print('coords:', x, y)
  
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        print('vals:', b, g, r)
        cv2.imshow('image', img)
  
    # checking for right mouse clicks     
    if event==cv2.EVENT_RBUTTONDOWN:
  
        # displaying the coordinates
        # on the Shell
        print('coords:', x, y)
  
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        print('vals:', b, g, r)
        cv2.imshow('image', img)
  
# driver function
if __name__=="__main__":
  
    # reading the image
    img = cv2.imread('data/img' + args.image_num + '.jpg', 1)
    
    if args.hsv:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
  
    # displaying the image
    cv2.imshow('image', img)
  
    # setting mouse handler for the image
    # and calling the click_event() function
    cv2.setMouseCallback('image', click_event)
  
    # wait for a key to be pressed to exit
    cv2.waitKey(0)
  
    # close the window
    cv2.destroyAllWindows()