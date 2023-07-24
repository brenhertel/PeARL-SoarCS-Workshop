import cv2
import numpy as np


yellow_lower = np.array([0, 0, 0])
yellow_upper = np.array([255, 255, 255])

green_lower = np.array([0, 0, 0])
green_upper = np.array([255, 255, 255])

#TODO: Change this function so that it filters the image based on color using the hsv range for each color.
def filter_image(img, hsv_lower, hsv_upper):

    # Convert from RGB to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # Modify mask
    mask = cv2.inRange(hsv, hsv_lower, hsv_upper)
    cv2.imshow('mask', mask)
    cv2.imshow('img', img)
    #cv2.waitKey(0)
    return mask


#TODO: Change the parameters to make blob detection more accurate. Hint: You might need to set some parameters to specify features such as color, size, and shape. The features have to be selected based on the application.
def detect_blob(mask):
    img = cv2.medianBlur(mask, 5)
    img = cv2.medianBlur(img, 5)

    cv2.imshow('blob', img)
   # Set up the SimpleBlobdetector with default parameters with specific values.
    params = cv2.SimpleBlobDetector_Params()

    params.filterByColor = True
    params.blobColor = 255
    params.filterByConvexity = False
    params.filterByInertia = False
    params.filterByArea = True
    params.minArea = 300
    params.maxArea = 100000

    # builds a blob detector with the given parameters
    detector = cv2.SimpleBlobDetector_create(params)

    # use the detector to detect blobs.
    keypoints = detector.detect(img)

    img_w_kp = cv2.drawKeypoints(img, keypoints, np.array([]), (0,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow("Keypoints", img_w_kp)
    # cv2.waitKey(0)

    return len(keypoints)


def count_cubes(img):
    mask_green = filter_image(img, green_lower, green_upper)
    num_green = detect_blob(mask_green)
    mask_yellow = filter_image(img, yellow_lower, yellow_upper)
    num_yellow = detect_blob(mask_yellow)
    #num_green = 1
    return num_yellow, num_green
