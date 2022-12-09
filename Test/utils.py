# Imports
import cv2 as cv
import numpy as np
import skimage.io as io
from skimage.color import rgb2gray,rgb2hsv,rgba2rgb
import matplotlib.pyplot as plt
import math

# Read RGB image uisng CV and result is a RGB image
def Read_RGB_Image(path):
    image=cv.imread(path,1)#cv2.IMREAD_COLOR: It specifies to load a color image. Any transparency of image will be neglected.
    # Converting BGR color to RGB color format
    RGB_img = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    return RGB_img


# Read RGB image uisng CV and result is a RGB image
def Read_GrayScale_Image(path):
    image=cv.imread(path,0)
    return image

# Show images in plot
def Show_Images(images,titles):
    # Create Figure
    fig=plt.figure(figsize=(20, 10))
    
    # Setting number of rows and columns
    columns=2 # 2columns
    rows=math.ceil(np.shape(images)[0]/columns) #No of rows    
    
    n=1 #Counter for the subplots order
    for image,title in zip(images,titles):
        #Add subplot @ order postion 
        fig.add_subplot(rows, columns, n)
        n+=1
        plt.axis('off')
        plt.title(title)
        plt.imshow(image)