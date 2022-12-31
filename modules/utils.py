# Imports
import cv2
import numpy as np
import pandas as pd
import skimage.io as io
import matplotlib.pyplot as plt
from skimage.color import rgb2gray,rgb2hsv
import math

import pytesseract
from sklearn import svm
from skimage.feature import hog


# Read RGB image uisng CV and result is a RGB image
def Read_RGB_Image(path):
    image=cv.imread(path,1)#cv2.IMREAD_COLOR: It specifies to load a color image. Any transparency of image will be neglected.
    # Converting BGR color to RGB color format
    RGB_img = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    return RGB_img

def show_images(images,titles=None):
    #This function is used to show image(s) with titles by sending an array of images and an array of associated titles.
    # images[0] will be drawn with the title titles[0] if exists
    # You aren't required to understand this function, use it as-is.
    n_ims = len(images)
    if titles is None: titles = ['(%d)' % i for i in range(1,n_ims + 1)]
    fig = plt.figure()
    n = 1
    for image,title in zip(images,titles):
        a = fig.add_subplot(1,n_ims,n)
        if image.ndim == 2: 
            plt.gray()
        plt.imshow(image)
        a.set_title(title)
        n += 1
    fig.set_size_inches(np.array(fig.get_size_inches()) * n_ims)
    plt.show()


def showHist(img):
    # An "interface" to matplotlib.axes.Axes.hist() method
    plt.figure()
    imgHist = histogram(img, nbins=256)
    
    bar(imgHist[1].astype(np.uint8), imgHist[0], width=0.8, align='center')


#Reorder 4 Points in clockwise order, starting from top left
def reorderPoints(points):

    points = points.reshape((4, 2))
    newPoints = np.zeros((4, 1, 2), dtype=np.int32)
    add = points.sum(1)

    newPoints[0] = points[np.argmin(add)]
    newPoints[3] =points[np.argmax(add)]
    diff = np.diff(points, axis=1)
    newPoints[1] =points[np.argmin(diff)]
    newPoints[2] = points[np.argmax(diff)]

    return newPoints
#Darw Reactangle
def drawRectangle(img,biggest,thickness):
    cv2.line(img, (biggest[0][0][0], biggest[0][0][1]), (biggest[1][0][0], biggest[1][0][1]), (0, 255, 0), thickness)
    cv2.line(img, (biggest[0][0][0], biggest[0][0][1]), (biggest[2][0][0], biggest[2][0][1]), (0, 255, 0), thickness)
    cv2.line(img, (biggest[3][0][0], biggest[3][0][1]), (biggest[2][0][0], biggest[2][0][1]), (0, 255, 0), thickness)
    cv2.line(img, (biggest[3][0][0], biggest[3][0][1]), (biggest[1][0][0], biggest[1][0][1]), (0, 255, 0), thickness)

    return img

# # Show images in plot
# def Show_Images(images,titles):
#     # Create Figure
#     fig=plt.figure(figsize=(20, 10))
    
#     # Setting number of rows and columns
#     columns=2 # 2columns
#     rows=math.ceil(np.shape(images)[0]/columns) #No of rows    
    
#     n=1 #Counter for the subplots order
#     for image,title in zip(images,titles):
#         #Add subplot @ order postion 
#         fig.add_subplot(rows, columns, n)
#         n+=1
#         plt.axis('off')
#         plt.title(title)
#         plt.imshow(image)
        
    

# # Function to sort points in a contour in clockwise order, starting from top left
# def processContour(approx):
#     # Reshape array([x, y], ...) to array( array([x], [y]), ...)
#     approx = approx.reshape((4, 2))

#     # Sort points in clockwise order, starting from top left
#     pts = np.zeros((4, 2), dtype=np.float32)

#     # Add up all values
#     # Smallest sum = top left point
#     # Largest sum = bottom right point
#     s = approx.sum(axis=1)
#     pts[0] = approx[np.argmin(s)]
#     pts[2] = approx[np.argmax(s)]

#     # For the other 2 points, compute difference between all points
#     # Smallest difference = top right point
#     # Largest difference = bottom left point
#     diff = np.diff(approx, axis=1)
#     pts[1] = approx[np.argmin(diff)]
#     pts[3] = approx[np.argmax(diff)]

#     # Calculate smallest height and width
#     width = int(min(pts[1][0] - pts[0][0], pts[2][0] - pts[3][0]))
#     height = int(min(pts[3][1] - pts[0][1], pts[2][1] - pts[1][1]))

#     return pts, width, height
